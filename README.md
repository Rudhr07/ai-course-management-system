# 🎓 AI Course Management System

> **Demo Video**: (https://drive.google.com/file/d/1i2hNeljiZyZt-EjmqYQrfsThlWAGfrgM/view)

A modern, AI-powered course management system built with Flask and integrated with Ollama for intelligent academic assistance.

**Developed by:** [Your Name]

---

## ✨ Features

### 🔐 **Authentication & User Management**
- Secure user registration and login system
- User profiles with college, degree, and study years
- Session management with Flask-Login

### 📚 **Course Management**
- **8 Semester Organization**: Pre-structured semester cards (Sem 1-8)
- **Complete CRUD Operations**: Add, edit, delete, and view courses
- **Course Details**: Name, description, credit hours for each course
- **Per-semester Organization**: Manage courses individually for each semester

### 🤖 **AI Assistant Integration**
- **Real-time AI Chat**: ChatGPT-like streaming responses
- **Context-Aware Guidance**: AI knows YOUR courses and provides personalized advice
- **Course Summarization**: AI-powered semester course summaries with study tips
- **Academic Search**: Intelligent answers based on your actual subjects
- **Dual Backend**: Ollama (local) or Groq API (cloud) integration

### 🎨 **Modern UI/UX**
- **Professional Design**: Clean, modern interface with gradient themes
- **Responsive Layout**: Mobile-friendly design
- **Interactive Dashboard**: Semester cards with course counts
- **Floating Chatbot**: Bottom-right AI assistant widget

---

## 🛠️ Technology Stack

### **Backend**
- **Flask 2.3.3** - Web framework
- **Flask-SQLAlchemy 3.0.3** - ORM and database management
- **Flask-Login 0.6.2** - User authentication and session management
- **SQLite** - Lightweight database
- **Werkzeug 2.3.7** - WSGI utilities

### **AI Integration**
- **Ollama** - Local LLM server (for local development)
- **Groq API** - Cloud-hosted Llama3 (for production/Vercel)
- **Llama3** - Language model for AI assistance
- **Requests 2.31.0** - HTTP client for API communication


### **Features**
- **Streaming Responses** - Real-time AI chat like ChatGPT
- **Responsive Design** - Mobile and desktop optimized
- **Professional Auth Pages** - Clean login/signup interface
- **Custom Logo Integration** - Favicon and branding support

---

## 🚀 Quick Start

### **Prerequisites**
- Python 3.8+
- Ollama installed and running locally
- Llama3 model available in Ollama

### **Installation**

1. **Clone and Setup**
   ```bash
   git clone <repository-url>
   cd ai-course-management
   ```

2. **Create Virtual Environment**
   ```bash
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1  # Windows
   # or
   source .venv/bin/activate     # Linux/Mac
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Start Ollama** (Required for AI features)
   ```bash
   ollama serve
   ollama pull llama3
   ```

5. **Run the Application**
   ```bash
   python app.py
   ```
   Or use the provided scripts:
   ```bash
   .\run.ps1    # Windows PowerShell
   .\run.bat    # Windows Command Prompt
   ```

6. **Access the App**
   Open http://localhost:5000 in your browser

---

## 📖 Usage Guide

### **Getting Started**
1. **Sign Up**: Create an account with your academic details
2. **Dashboard**: View all 8 semesters on the main dashboard
3. **Add Courses**: Click on any semester to add/manage courses (include descriptions!)
4. **AI Assistant**: Use the floating chat widget for personalized academic help

### **AI Assistant Features**
- **Context-Aware**: AI has access to ALL your semester courses and descriptions
- **Personalized Answers**: "How should I prepare for finals?" → Gets advice specific to YOUR subjects
- **Course Connections**: "How do my courses relate?" → AI analyzes your actual coursework
- **Study Planning**: "Create a study plan" → Tailored to your current semester
- **Career Guidance**: "What jobs fit my courses?" → Based on your actual subjects

**💡 Pro Tip**: Add detailed course descriptions for better AI assistance!

### **Example Questions**
- "What should I focus on this semester?"
- "How do my Data Structures and Algorithms courses connect?"
- "Explain concepts from my Machine Learning course"
- "What career paths match my coursework?"

---

## 🔧 Configuration

### **Environment Variables**
```bash
SECRET_KEY=your-secret-key          # Flask secret key (required)
GROQ_API_KEY=gsk_xxx                # Groq API key (for cloud deployment)
GROQ_MODEL=llama-3.3-70b-versatile  # Groq model (optional)
OLLAMA_HOST=http://localhost:11434  # Ollama server URL (local only)
OLLAMA_MODEL=llama3                 # Ollama model name (local only)
```

### **AI Backend Priority**
- **With GROQ_API_KEY set**: Uses Groq Cloud API (works on Vercel, Railway, etc.)
- **Without GROQ_API_KEY**: Falls back to local Ollama server

### **Database**
- Automatically creates `cms.db` on first run
- No manual database setup required

---

## ☁️ Cloud Deployment (Vercel)

### **Prerequisites**
1. Get a **free Groq API key** from [console.groq.com](https://console.groq.com/)
2. Install [Vercel CLI](https://vercel.com/cli) or use the web dashboard

### **Deploy Steps**

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Ready for deployment"
   git push origin main
   ```

2. **Import to Vercel**
   - Go to [vercel.com](https://vercel.com)
   - Click "New Project" → Import your GitHub repo

3. **Set Environment Variables** in Vercel Dashboard:
   ```
   SECRET_KEY = your-random-secret-key
   GROQ_API_KEY = gsk_your_groq_api_key
   ```

4. **Deploy!** Vercel will auto-build and deploy

### **Why Groq for Cloud?**
- ✅ **Ollama can't run on Vercel** (requires persistent server + GPU)
- ✅ **Groq is FREE** with generous rate limits
- ✅ **Same Llama3 model** - identical AI capabilities
- ✅ **Faster inference** - Groq's LPU technology

---

## 📁 Project Structure

```
ai-course-management/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── vercel.json           # Vercel deployment config
├── .env.example          # Environment variables template
├── logo.png              # Custom logo
├── run.ps1 / run.bat     # Launch scripts
├── templates/            # HTML templates
│   ├── base.html         # Base template with styling
│   ├── login.html        # Authentication pages
│   ├── signup.html
│   ├── dashboard.html    # Main dashboard
│   ├── semester.html     # Semester management
│   ├── profile.html      # User profile
│   └── ...
├── static/
│   └── js/
│       └── chatbot.js    # AI chat functionality
└── instance/
    └── cms.db            # SQLite database (auto-created)
```

---

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

**Built with ❤️ by Rudhr Chauhan**
