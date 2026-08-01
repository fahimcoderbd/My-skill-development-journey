# Django Apps Configuration Guide

## Adding a New App

### Step 1: Create the App
```bash
python manage.py startapp my_apps.new_app_name
```

### Step 2: Register in Settings
Edit `myweb/settings.py`:
```python
INSTALLED_APPS = [
    ...
    'my_apps.new_app_name',
]
```

### Step 3: Create URLs
Create `my_apps/new_app_name/urls.py`:
```python
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
```

### Step 4: Add to Main URLs
Edit `myweb/urls.py`:
```python
urlpatterns = [
    ...
    path('new_app/', include('my_apps.new_app_name.urls')),
]
```

### Step 5: Create Templates & Static
- Templates: `templates/new_app_name/`
- Static: `static/new_app_name/`

## Models Convention

**File Location**: `my_apps/<app_name>/models.py`

```python
from django.db import models

class MyModel(models.Model):
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        verbose_name = "My Model"
        verbose_name_plural = "My Models"
        ordering = ['-created_at']
    
    def __str__(self):
        return self.name
```

## Views Convention

**File Location**: `my_apps/<app_name>/views.py`

```python
from django.shortcuts import render
from django.http import JsonResponse
from . import models

def list_view(request):
    objects = models.MyModel.objects.all()
    return render(request, 'app_name/list.html', {'objects': objects})
```

## Admin Registration

**File Location**: `my_apps/<app_name>/admin.py`

```python
from django.contrib import admin
from . import models

@admin.register(models.MyModel)
class MyModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'created_at']
    search_fields = ['name']
    list_filter = ['created_at']
```

## Template Hierarchy

```
templates/
├── homeapp/
│   ├── base.html           # App-specific base template
│   ├── home.html
│   └── ...
└── studentapp/
    ├── list.html
    └── ...
```

Template Usage in Views:
```python
return render(request, 'homeapp/home.html', context)
```

## Static Files Organization

```
static/
├── homeapp/
│   ├── css/
│   │   ├── base.css
│   │   └── responsive.css
│   └── js/
│       ├── main.js
│       └── utils.js
└── studentapp/
    ├── css/
    └── js/
```

Template Usage:
```html
{% load static %}
<link rel="stylesheet" href="{% static 'homeapp/css/base.css' %}">
<script src="{% static 'homeapp/js/main.js' %}"></script>
```

## Database Migrations

```bash
# Create migrations for changes
python manage.py makemigrations

# Apply migrations
python manage.py migrate

# Show migration status
python manage.py showmigrations

# Revert to previous migration
python manage.py migrate app_name 0001
```

## Testing

```bash
# Run all tests
python manage.py test

# Run specific app tests
python manage.py test my_apps.homeapp

# Run with verbosity
python manage.py test --verbosity=2
```

## Development Workflow

```bash
# 1. Make model changes
# 2. Create migrations
python manage.py makemigrations

# 3. Review migrations
cat my_apps/homeapp/migrations/0003_auto_*.py

# 4. Apply migrations
python manage.py migrate

# 5. Run development server
python manage.py runserver

# 6. Test in browser
# Visit http://localhost:8000/
```

---
**Best Practices:**
- ✅ Keep business logic in models
- ✅ Keep view logic simple and DRY
- ✅ Use meaningful variable names
- ✅ Write tests for critical features
- ✅ Document complex functions
- ✅ Use transactions for multi-step DB operations
