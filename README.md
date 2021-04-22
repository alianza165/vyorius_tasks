
# vyorius_tasks
Job app

# Requirements
Python==3.6.9
Django==2.2.13
django-crispy-forms==1.7.2
Pillow==5.2.0
requests==2.19.1

# How to run
1. Go to folder containing manage.py file.
2. Once in the directory execute the following code: python manage.py runserver
3. Go to localhost:8000 on web browser

# For password reset option:
1. Make sure you have a google account with 2-factor authentication
2. Open file vyorius_tasks/django_project/settings.py
3. Replace EMAIL_HOST_USER and EMAIL_HOST_PASSWORD values with your "*email address*" and "*google app password*"
4. Save the file
