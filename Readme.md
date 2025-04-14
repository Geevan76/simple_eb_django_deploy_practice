# Django User Authentication and Profile Management with AWS S3 Integration

This project demonstrates how to build a Django web application with user authentication, profile management, and AWS S3 integration for static and media file storage. The guide is structured to help developers understand each component and its purpose.

## Table of Contents
1. [Project Setup](#project-setup)
2. [User Authentication](#user-authentication)
3. [Profile Management](#profile-management)
4. [Static and Media Files](#static-and-media-files)
5. [AWS S3 Integration](#aws-s3-integration)
6. [Development vs Production Settings](#development-vs-production-settings)
7. [Common Issues and Solutions](#common-issues-and-solutions)

## Project Setup

### Initial Setup
```bash
# Create a virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Unix or MacOS:
source venv/bin/activate

# Install required packages
pip install django django-environ boto3 django-storages pillow

# Create Django project
django-admin startproject project_1

# Create Django app
python manage.py startapp app_1
```

### Project Structure
```
project_root/
│
├── project_1/                 # Main project directory
│   ├── settings.py           # Project settings
│   ├── urls.py               # Main URL configuration
│   └── wsgi.py              # WSGI configuration
│
├── app_1/                    # Main application
│   ├── models.py            # Database models
│   ├── views.py             # View functions
│   ├── forms.py             # Form definitions
│   ├── urls.py              # App URL configuration
│   └── templates/           # HTML templates
│       └── app_1/
│           ├── home.html
│           ├── dashboard.html
│           └── edit_profile.html
│
├── static/                   # Static files directory
│   ├── css/
│   │   └── styles.css
│   └── images/
│       └── default.jpg
│
├── manage.py                 # Django management script
└── requirements.txt         # Project dependencies
```

## User Authentication

### Models (models.py)
```python
from django.db import models
from django.contrib.auth.models import User

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(null=True, blank=True, default='default.jpg', upload_to='')

    def __str__(self):
        return f"{self.user.username}'s Profile"
```

### Why OneToOneField?
- Creates a one-to-one relationship between User and Profile
- Each user has exactly one profile and vice versa
- Allows extending User model without modifying Django's built-in User model
- Maintains database integrity with CASCADE deletion

### Forms (forms.py)
```python
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email']

class UserEmailForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['email']

class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_pic']
```

### Why Custom Forms?
- Extends Django's built-in forms for customization
- Separates concerns between user data and profile data
- Enables form validation and clean data handling
- Provides structured way to handle file uploads

## Static and Media Files

### Settings Configuration
```python
# Static files configuration
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    BASE_DIR / 'static',
]
STATIC_ROOT = BASE_DIR / 'staticfiles'

# Media files configuration
MEDIA_URL = '/images/'
MEDIA_ROOT = BASE_DIR / 'static/images'
```

### Why These Settings?
- STATIC_URL: URL prefix for serving static files
- STATICFILES_DIRS: Where Django looks for static files
- STATIC_ROOT: Where collectstatic command collects files
- MEDIA_URL/ROOT: Similar concept for user-uploaded files

## AWS S3 Integration

### AWS Setup
1. Create an S3 bucket
2. Configure IAM user with appropriate permissions
3. Get access keys for authentication

### Settings Configuration
```python
AWS_ACCESS_KEY_ID = env('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = env('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = f'{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com'
AWS_S3_FILE_OVERWRITE = False

STORAGES = {
    "default": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
    "staticfiles": {
        "BACKEND": "storages.backends.s3boto3.S3Boto3Storage",
    },
}
```

### Why Use S3?
- Scalable storage solution
- Reliable content delivery
- Separates storage from application servers
- Cost-effective for growing applications

## Development vs Production Settings

### Using Environment Variables
```python
import environ

env = environ.Env(
    DEBUG=(bool, False)
)
environ.Env.read_env()

# Use environment variables
SECRET_KEY = env('SECRET_KEY')
DEBUG = env('DEBUG')
```

### Why Environment Variables?
- Keeps sensitive data out of version control
- Enables different configurations per environment
- Follows security best practices
- Makes deployment more flexible

## Common Issues and Solutions

### Static Files Not Loading
1. Check STATIC_ROOT and STATIC_URL settings
2. Run python manage.py collectstatic
3. Verify AWS credentials if using S3
4. Check file permissions

### Profile Picture Upload Issues
1. Verify MEDIA_ROOT exists
2. Check file upload_to path in model
3. Ensure form has enctype="multipart/form-data"
4. Verify S3 bucket permissions

### Database Migration Issues
1. Make migrations: `python manage.py makemigrations`
2. Apply migrations: `python manage.py migrate`
3. Check for conflicting migrations
4. Consider using --fake flag if needed

## Version Control Best Practices

### Branch Management
```bash
# Create feature branch
git checkout -b feature/profile-pictures

# Stage changes
git add .

# Commit changes
git commit -m "Add profile picture feature"

# Push to remote
git push -u origin feature/profile-pictures
```

### Why Branch?
- Isolates feature development
- Enables parallel development
- Makes code review easier
- Simplifies rollback if needed

## Deployment Checklist

1. Set DEBUG=False in production
2. Configure proper ALLOWED_HOSTS
3. Use secure HTTPS connections
4. Set up proper static file serving
5. Configure database settings
6. Set up proper logging
7. Review security settings

## Contributing

Please read CONTRIBUTING.md for details on our code of conduct and the process for submitting pull requests.

## License

This project is licensed under the MIT License - see the LICENSE.md file for details