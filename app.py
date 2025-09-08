from flask import Flask, render_template, request, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from werkzeug.security import generate_password_hash, check_password_hash
import os
import requests

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('CMS_SECRET', 'dev-secret')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cms.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


# Models
class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(256), nullable=False)
    college = db.Column(db.String(256))
    degree = db.Column(db.String(128))
    years = db.Column(db.String(64))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)


class Course(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    semester = db.Column(db.Integer, nullable=False)
    name = db.Column(db.String(256), nullable=False)
    description = db.Column(db.Text)
    credits = db.Column(db.Integer, default=3)

    user = db.relationship('User', backref='courses')


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


# AI helpers using Ollama (local Llama3). Expects an Ollama server running locally.
import json

OLLAMA_HOST = os.environ.get('OLLAMA_HOST', 'http://localhost:11434')
OLLAMA_MODEL = os.environ.get('OLLAMA_MODEL', 'llama3')  # adjust to your local model name


def call_ollama(prompt, model=None, max_tokens=200):
    """Call local Ollama server /api/generate with a prompt and return text output."""
    model = model or OLLAMA_MODEL
    url = f"{OLLAMA_HOST}/api/generate"
    headers = {'Content-Type': 'application/json'}
    body = {
        'model': model,
        'prompt': prompt,
        'stream': False,  # Get complete response at once
        'options': {
            'num_predict': max_tokens,
            'temperature': 0.3,  # Lower for faster, more focused responses
            'top_p': 0.9,
            'repeat_penalty': 1.1
        }
    }
    try:
        resp = requests.post(url, headers=headers, json=body, timeout=30)  # Reduced timeout
        resp.raise_for_status()
        data = resp.json()
        # Ollama returns response in 'response' field
        if isinstance(data, dict) and 'response' in data:
            return data['response'].strip()
        # fallback
        return f"Unexpected response format: {data}"
    except requests.exceptions.Timeout:
        return "AI response timed out. Please try a shorter question or check if Ollama is running properly."
    except requests.exceptions.ConnectionError:
        return "Cannot connect to Ollama. Please ensure Ollama is running on localhost:11434"
    except Exception as e:
        # On failure, return a helpful message for UI
        return f"AI service error: {str(e)}"


def ai_search(query):
    """Return (answer_text, resources_list) where resources_list is [{'title','url'}, ...]."""
    prompt = f"Answer briefly: {query}\n\nProvide a concise explanation in 2-3 sentences."
    text = call_ollama(prompt, max_tokens=150)
    # Simplified resources since AI might not generate valid URLs
    resources = [
        {"title": "Wikipedia", "url": f"https://en.wikipedia.org/wiki/{query.replace(' ', '_')}"},
        {"title": "Khan Academy", "url": "https://www.khanacademy.org"},
        {"title": "Coursera", "url": "https://www.coursera.org"}
    ]
    return text, resources


def ai_summarize(semester, courses):
    names = [c.name for c in courses]
    if not names:
        return f"No courses found for Semester {semester}. Add some courses first!"
    
    prompt = f"Briefly summarize these courses for semester {semester}: {', '.join(names)}. Give 2 sentences and 2 study tips."
    text = call_ollama(prompt, max_tokens=100)
    return text


# Routes
@app.route('/')
def index():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
    return render_template('index.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        college = request.form.get('college')
        degree = request.form.get('degree')
        years = request.form.get('years')
        if User.query.filter_by(email=email).first():
            flash('Email already registered')
            return redirect(url_for('signup'))
        user = User(email=email, college=college, degree=degree, years=years)
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        login_user(user)
        return redirect(url_for('dashboard'))
    return render_template('signup.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']
        user = User.query.filter_by(email=email).first()
        if user and user.check_password(password):
            login_user(user)
            return redirect(url_for('dashboard'))
        flash('Invalid credentials')
        return redirect(url_for('login'))
    return render_template('login.html')


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('index'))


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    if request.method == 'POST':
        current_user.college = request.form.get('college')
        current_user.degree = request.form.get('degree')
        current_user.years = request.form.get('years')
        db.session.commit()
        flash('Profile updated')
        return redirect(url_for('dashboard'))
    return render_template('profile.html')


@app.route('/dashboard')
@login_required
def dashboard():
    semesters = list(range(1, 9))
    return render_template('dashboard.html', semesters=semesters)


@app.route('/semester/<int:sem>')
@login_required
def semester_view(sem):
    courses = Course.query.filter_by(user_id=current_user.id, semester=sem).all()
    return render_template('semester.html', semester=sem, courses=courses)


@app.route('/semester/<int:sem>/add', methods=['POST'])
@login_required
def add_course(sem):
    name = request.form.get('name')
    description = request.form.get('description')
    credits = int(request.form.get('credits') or 3)
    course = Course(user_id=current_user.id, semester=sem, name=name, description=description, credits=credits)
    db.session.add(course)
    db.session.commit()
    flash('Course added')
    return redirect(url_for('semester_view', sem=sem))


@app.route('/course/<int:course_id>/edit', methods=['GET', 'POST'])
@login_required
def edit_course(course_id):
    course = Course.query.get_or_404(course_id)
    if course.user_id != current_user.id:
        flash('Not authorized')
        return redirect(url_for('dashboard'))
    if request.method == 'POST':
        course.name = request.form.get('name')
        course.description = request.form.get('description')
        course.credits = int(request.form.get('credits') or 3)
        db.session.commit()
        flash('Course updated')
        return redirect(url_for('semester_view', sem=course.semester))
    return render_template('edit_course.html', course=course)


@app.route('/course/<int:course_id>/delete', methods=['POST'])
@login_required
def delete_course(course_id):
    course = Course.query.get_or_404(course_id)
    if course.user_id != current_user.id:
        flash('Not authorized')
        return redirect(url_for('dashboard'))
    sem = course.semester
    db.session.delete(course)
    db.session.commit()
    flash('Course deleted')
    return redirect(url_for('semester_view', sem=sem))



from flask import Response, stream_with_context, jsonify

def stream_ollama_response(prompt, model=None, max_tokens=200):
    """Stream response from Ollama for real-time chat UI."""
    model = model or OLLAMA_MODEL
    url = f"{OLLAMA_HOST}/api/generate"
    headers = {'Content-Type': 'application/json'}
    body = {
        'model': model,
        'prompt': prompt,
        'stream': True,
        'options': {
            'num_predict': max_tokens,
            'temperature': 0.3,
            'top_p': 0.9,
            'repeat_penalty': 1.1
        }
    }
    try:
        with requests.post(url, headers=headers, json=body, stream=True, timeout=60) as resp:
            resp.raise_for_status()
            for line in resp.iter_lines():
                if line:
                    try:
                        data = json.loads(line.decode('utf-8'))
                        if 'response' in data:
                            yield data['response']
                    except Exception:
                        continue
    except Exception as e:
        yield f"[AI error: {str(e)}]"

@app.route('/ai/summarize', methods=['POST'])
@login_required
def ai_summarize_route():
    sem = int(request.form.get('semester'))
    courses = Course.query.filter_by(user_id=current_user.id, semester=sem).all()
    names = [c.name for c in courses]
    if not names:
        return jsonify({"result": f"No courses found for Semester {sem}. Add some courses first!"})
    prompt = f"Briefly summarize these courses for semester {sem}: {', '.join(names)}. Give 2 sentences and 2 study tips."
    def generate():
        for chunk in stream_ollama_response(prompt, max_tokens=100):
            yield chunk
    return Response(stream_with_context(generate()), mimetype='text/plain')


@app.route('/ai/search', methods=['POST'])
@login_required
def ai_search_route():
    query = request.form.get('query')
    prompt = f"Answer briefly: {query}\n\nProvide a concise explanation in 2-3 sentences."
    def generate():
        for chunk in stream_ollama_response(prompt, max_tokens=150):
            yield chunk
    return Response(stream_with_context(generate()), mimetype='text/plain')


def init_db():
    # Ensure we create tables within the Flask application context
    with app.app_context():
        db.create_all()


if __name__ == '__main__':
    init_db()
    app.run(debug=True)
