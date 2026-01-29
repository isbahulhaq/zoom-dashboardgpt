# 🎥 Zoom Dashboard

A modern, responsive dashboard application for managing and tracking Zoom meetings, built with Flask and deployed on Render.

## ✨ Features

- 📊 Real-time meeting statistics and analytics
- 📅 View today's scheduled meetings
- 👥 Track active users and participants
- ⏰ Monitor total meeting hours
- 🔄 Auto-refresh functionality (every 30 seconds)
- 📱 Fully responsive design for all devices
- 🔌 RESTful API endpoints
- ❤️ Health check endpoint for monitoring

## 🚀 Live Demo

Visit the live application: [https://zoom-dashboard-1.onrender.com/](https://zoom-dashboard-1.onrender.com/)

## 🛠️ Technology Stack

- **Backend:** Python 3.11, Flask 3.0
- **Web Server:** Gunicorn
- **Frontend:** HTML5, CSS3, JavaScript (Vanilla)
- **Deployment:** Render (with Docker support)
- **Version Control:** Git/GitHub

## 📋 Prerequisites

Before you begin, ensure you have the following installed:
- Python 3.11 or higher
- pip (Python package manager)
- Git

## 🔧 Local Development Setup

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/zoom-dashboard.git
cd zoom-dashboard
```

### 2. Create Virtual Environment

```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Application

```bash
# Development mode
python app.py

# Or using Gunicorn (production-like)
gunicorn app:app --bind 0.0.0.0:5000
```

The application will be available at `http://localhost:5000`

## 🌐 Deployment on Render

### Method 1: Automatic Deployment (Recommended)

1. **Fork/Upload this repository to your GitHub account**

2. **Create a new Web Service on Render:**
   - Go to [Render Dashboard](https://dashboard.render.com/)
   - Click "New +" → "Web Service"
   - Connect your GitHub repository

3. **Configure the service:**
   - **Name:** zoom-dashboard (or your preferred name)
   - **Region:** Choose closest to your users
   - **Branch:** main
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `gunicorn app:app --bind 0.0.0.0:$PORT --workers 2 --timeout 120`
   - **Plan:** Free

4. **Environment Variables (Optional):**
   - `SECRET_KEY`: (Auto-generated is fine)
   - `DEBUG`: False
   - `PYTHON_VERSION`: 3.11.0

5. **Click "Create Web Service"**

Render will automatically detect the `.render.yaml` file and deploy your application!

### Method 2: Using Render.yaml

The repository includes a `.render.yaml` file that automatically configures everything. Just connect your repo and Render will handle the rest!

### Method 3: Using Docker

Render will automatically detect the `Dockerfile` and use it for deployment.

## 📁 Project Structure

```
zoom-dashboard/
│
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Dockerfile            # Docker configuration
├── .render.yaml          # Render deployment config
├── runtime.txt           # Python version specification
├── Procfile              # Process file for deployment
├── .gitignore           # Git ignore rules
│
├── templates/            # HTML templates
│   ├── index.html       # Main dashboard page
│   ├── about.html       # About page
│   ├── 404.html         # 404 error page
│   └── 500.html         # 500 error page
│
└── README.md            # This file
```

## 🔌 API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/` | GET | Main dashboard page |
| `/about` | GET | About page |
| `/api/stats` | GET | Get dashboard statistics (JSON) |
| `/api/meetings` | GET | Get meetings list (JSON) |
| `/health` | GET | Health check endpoint |

### Example API Response

**GET /api/stats**
```json
{
  "total_meetings": 150,
  "active_users": 45,
  "total_hours": 320,
  "upcoming_meetings": 12
}
```

**GET /api/meetings**
```json
[
  {
    "id": 1,
    "title": "Team Standup",
    "time": "10:00 AM",
    "duration": "30 mins",
    "participants": 8
  },
  ...
]
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### 1. Application not starting on Render
- **Check logs:** Render Dashboard → Your Service → Logs
- **Verify:** `PORT` environment variable is being used correctly
- **Ensure:** Gunicorn is installed in `requirements.txt`

#### 2. Templates not found
- **Check:** `templates` folder exists and is not in `.gitignore`
- **Verify:** Folder name is lowercase `templates` not `Templates`

#### 3. Static files not loading
- **Ensure:** Files are committed to Git
- **Check:** Paths are correct in HTML templates

#### 4. Database connection issues
- For SQLite: Use absolute paths
- For PostgreSQL: Use Render's database service

## 🔒 Security Considerations

- Never commit `.env` files or secrets to Git
- Always use environment variables for sensitive data
- Set `DEBUG=False` in production
- Use strong `SECRET_KEY` values
- Keep dependencies updated

## 📝 Environment Variables

| Variable | Description | Default |
|----------|-------------|---------|
| `PORT` | Application port | 5000 |
| `DEBUG` | Debug mode | False |
| `SECRET_KEY` | Flask secret key | Auto-generated |
| `PYTHON_VERSION` | Python version | 3.11.0 |

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

## 👨‍💻 Author

Built with ❤️ by [Your Name]

## 🙏 Acknowledgments

- Flask framework
- Render platform
- All contributors and users

## 📞 Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the [Render documentation](https://render.com/docs)
- Review Flask documentation at [flask.palletsprojects.com](https://flask.palletsprojects.com/)

---

**Happy Coding! 🚀**
