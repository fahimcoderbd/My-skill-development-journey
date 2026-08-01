# My Website - Django Project

## 📁 Project Structure

```
My_website/
│
├── manage.py                 # Django management script
├── db.sqlite3               # SQLite database
├── requirements.txt         # Python dependencies
├── run.bat                  # Batch script to run the server
│
├── myweb/                   # Project configuration
│   ├── __init__.py
│   ├── settings.py          # Django settings (INSTALLED_APPS, TEMPLATES, STATIC, etc.)
│   ├── urls.py              # Main URL routing
│   ├── asgi.py              # ASGI configuration
│   └── wsgi.py              # WSGI configuration
│
├── my_apps/                 # 📦 Centralized apps directory
│   ├── __init__.py
│   │
│   ├── homeapp/             # Home application
│   │   ├── migrations/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py        # Database models
│   │   ├── views.py         # View logic
│   │   ├── urls.py          # App-level URL routing
│   │   └── tests.py
│   │
│   └── studentapp/          # Student management application
│       ├── migrations/
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── models.py
│       ├── views.py
│       ├── urls.py
│       └── tests.py
│
├── templates/               # 🎨 Centralized templates (root-level)
│   ├── homeapp/
│   │   ├── base.html
│   │   ├── home.html
│   │   ├── about.html
│   │   ├── contact.html
│   │   └── contact_view.html
│   │
│   └── studentapp/
│       ├── add_student.html
│       ├── show_students.html
│       ├── update_a_student.html
│       └── delete_student.html
│
├── static/                  # 📦 Centralized static files (root-level)
│   ├── homeapp/
│   │   ├── css/
│   │   │   └── styles.css
│   │   └── js/
│   │       └── main.js
│   │
│   └── studentapp/
│       ├── css/
│       └── js/
│
└── myweb_config/            # Configuration files (if needed)
```

## 🎯 Architecture Benefits

✅ **Scalable**: Multiple apps organized in `my_apps/`  
✅ **DRY**: Centralized `templates/` and `static/` directories  
✅ **Professional**: Standard Django project structure  
✅ **Maintainable**: Clear separation of concerns  
✅ **Flexible**: Easy to add new apps  

## 🚀 Quick Start

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py migrate
```

### Start development server
```bash
python manage.py runserver
```
Or use the batch script:
```bash
./run.bat
```

### Access the application
- Home: `http://localhost:8000/`
- About: `http://localhost:8000/about/`
- Contact: `http://localhost:8000/contact/`
- Student Management: `http://localhost:8000/student/`
- Admin Panel: `http://localhost:8000/admin/`

## 📱 Applications

### 1. **homeapp** (Home Application)
- Routes: `/`, `/about/`, `/contact/`, `/contact_info/`
- Features: Home page, About section, Contact form with data storage

### 2. **studentapp** (Student Management)
- Routes: `/student/add_student/`, `/student/show_students/`, etc.
- Features: Add, view, update, and delete student records

## ⚙️ Settings Reference

**INSTALLED_APPS**
```python
'my_apps.homeapp',
'my_apps.studentapp',
```

**TEMPLATES**
- DIRS: `templates/` (root-level)
- APP_DIRS: ✅ Enabled (for Django built-in templates)

**STATIC FILES**
- STATIC_URL: `/static/`
- STATICFILES_DIRS: Points to root-level `static/` folder
- STATIC_ROOT: `staticfiles/` (for production)

## 🔐 Security Notes

⚠️ **Before Deployment:**
1. Set `DEBUG = False`
2. Update `ALLOWED_HOSTS`
3. Generate a new `SECRET_KEY`
4. Use environment variables for sensitive data
5. Configure proper database (PostgreSQL, MySQL)
6. Set up HTTPS/SSL
7. Configure CORS if needed

## 📚 Additional Resources

- Django Docs: https://docs.djangoproject.com/
- Django Best Practices: https://wiki.python.org/moin/PythonSpeed
- Deployment Guide: https://docs.djangoproject.com/en/6.0/howto/deployment/

---
**Project**: My Website  
**Django Version**: 6.0.4  
**Python Version**: 3.13+  
