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
- **Course Summarization**: AI-powered semester course summaries
- **Academic Search**: Intelligent search and academic assistance
- **Ollama Integration**: Local LLM (Llama3) for privacy and speed

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
- **Ollama** - Local LLM server
- **Llama3** - Language model for AI assistance
- **Requests 2.31.0** - HTTP client for API communication

### **Frontend**
- **Bootstrap 5.3** - UI framework
- **Inter Font** - Modern typography
- **Custom CSS** - Professional styling and animations
- **Vanilla JavaScript** - Interactive features and real-time chat

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
3. **Add Courses**: Click on any semester to add/manage courses
4. **AI Assistant**: Use the floating chat widget for academic help

### **AI Assistant Commands**
- **General Questions**: "Explain data structures"
- **Course Summaries**: Select a semester and click "Summarize"
- **Study Tips**: "How should I study for exams?"
- **Academic Planning**: "Help me plan my semester"

---

## 🔧 Configuration

### **Environment Variables**
```bash
CMS_SECRET=your-secret-key          # Flask secret key
OLLAMA_HOST=http://localhost:11434  # Ollama server URL
OLLAMA_MODEL=llama3                 # AI model name
```

### **Database**
- Automatically creates `cms.db` on first run
- No manual database setup required

---

## 📁 Project Structure

```
ai-course-management/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
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
└── cms.db               # SQLite database (auto-created)
```

---

## 🤝 Contributing

Feel free to submit issues, fork the repository, and create pull requests for any improvements.

---

## 📝 License

This project is open source and available under the [MIT License](LICENSE).

---

**Built with ❤️ by [Your Name]**
