# Django Polls App with AWS Elastic Beanstalk Deployment

This project is a deployment of the **Django Polls app** to **AWS Elastic Beanstalk** as part of coursework.  
It demonstrates how to package, configure, and deploy a Django application to a cloud environment.

---

## 🚀 Deployment Details
- **Framework**: Django (Python 3.13)  
- **Platform**: AWS Elastic Beanstalk (Amazon Linux 2023)  
- **Database**: SQLite (for demo purposes)  
- **Static Files**: Served with [Whitenoise](https://whitenoise.readthedocs.io/)  

Live demo: 👉 [Polls App on AWS EB](http://swe1-env.eba-45zkrqrp.us-east-1.elasticbeanstalk.com/polls/)  

---

## 📂 Project Structure
swe1-app/
│── mysite/ # Django project settings and URLs
│── polls/ # Polls app with models, views, templates
│── manage.py # Django project management script
│── requirements.txt # Python dependencies
│── .ebextensions/ # Elastic Beanstalk configuration


---

## ⚡ Running Locally
1. Clone the repo:
   ```bash
   git clone https://github.com/SamKh5/django-polls-app.git
   cd django-polls-app

2. Create & activate virtual environment:

python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

3. Install dependencies:

pip install -r requirements.txt

4. Install dependencies:

pip install -r requirements.txt

5. Start the dev server:

python manage.py runserver

✅ Features

Basic Django polls app (vote on questions).

Admin panel with authentication.

Deployed to AWS with Elastic Beanstalk.
