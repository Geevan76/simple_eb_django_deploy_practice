# Django Project Deployment to AWS (Step-by-Step)

This guide captures the full step-by-step development and deployment process of a Django project, using AWS services such as Elastic Beanstalk (EB), RDS, and (upcoming) S3 for static/media files.

---

## ✅ COMPLETED STEPS

### 1. **Initialize Django Project**
- Created a fresh Django project and app (e.g., `app_1`).
- Verified homepage loads with minimal routing.

### 2. **Authentication System (Barebones)**
- Built using Django's built-in `User` model and `UserCreationForm`.
- Function-based views used for:
  - Register (`/register/`)
  - Login (`/login/`)
  - Logout (`/logout/`)
  - Dashboard (`/dashboard/`)
- Auto-login after registration
- Minimal templates under `app_1/templates/app_1/`

### 3. **Edit Profile Using Only User.email**
- Removed `email` from the `Profile` model
- Created `UserEmailForm` that directly edits `User.email`
- Simplified `edit_profile_view` to use `UserEmailForm`
- Ensured email is now consistent between user and admin view

### 4. **Switched from SQLite to RDS (PostgreSQL)**
- Installed `psycopg2-binary`
- Updated `DATABASES` in `settings.py` to point to AWS RDS
- Ran migrations + created superuser
- Tested full app against RDS

### 5. **Deployment to Elastic Beanstalk**
- Ran `eb init` and `eb create`
- Used `eb deploy --staged` for deployment without requiring Git commits
- App now runs on AWS EB and connects to RDS backend

### 6. **Schema Fix via pgAdmin**
- Connected to RDS using pgAdmin
- Manually added missing `email` column via SQL:
  ```sql
  ALTER TABLE app_1_profile ADD COLUMN email varchar(254);
  ```
- Verified `/dashboard/` now loads correctly

### 7. **Refactored to Use Only One Email Source**
- Removed `Profile.email` field and migration
- Created a single `UserEmailForm` that updates `User.email`
- Verified edit form and admin now reflect the same value

---

## 🔜 UPCOMING TASKS

### 8. **Static File Handling with S3**
- Configure `django-storages`
- Push static files to S3
- Set `STATIC_URL` to S3 bucket URL
- Test rendering in deployed app

### 9. **Media File Support (Profile Image Uploads)**
- Add `ImageField` to `Profile`
- Upload to S3
- Set default profile image
- Update dashboard to display image
- Update form to allow image upload

### 10. **Styling and UI Polish**
- Add base template with consistent navbar/footer
- Use TailwindCSS or simple custom CSS
- Refactor templates for layout, colors, spacing

### 11. **Best Practices for Production**
- Secure secrets using environment variables
- Use `.env` file or EB config settings for RDS credentials
- Set `DEBUG=False` in production
- Define proper `ALLOWED_HOSTS`
- Enable HTTPS on Elastic Beanstalk

---

## ✅ Folder Structure Summary (for Practice)

```bash
StartFromScratch/
├── app_1/
│   ├── templates/
│   │   └── app_1/
│   │       ├── home.html
│   │       ├── login.html
│   │       ├── register.html
│   │       ├── dashboard.html
│   │       ├── logged_out.html
│   │       └── edit_profile.html
│   ├── views.py
│   ├── models.py
│   ├── urls.py
│   ├── forms.py
│   ├── signals.py
├── manage.py
├── requirements.txt
├── .ebextensions/
├── .ebignore
└── settings.py
```

---

## ✅ Summary
This project is designed for repeated practice:
- Starts simple (barebones auth)
- Gradually integrates real-world services (RDS, S3)
- Keeps everything testable and deployable step-by-step
- Now cleaned up to avoid duplicate fields (one `User.email`)

Next up: connect static files to S3 🔜
