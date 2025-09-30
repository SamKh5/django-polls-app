# Django Polls App 🚀

A simple Django polls application deployed on **AWS Elastic Beanstalk**.  
This project demonstrates Django setup, database migrations, static files handling, and deployment to AWS.

---

## 📦 Deployment Details

- **Framework**: Django (Python 3.13)  
- **Platform**: AWS Elastic Beanstalk (Amazon Linux 2023)  
- **Database**: SQLite (for demo purposes)  

Live demo: 👉 [Polls App on AWS EB](http://swe1-env.eba-45zkrqrp.us-east-1.elasticbeanstalk.com/polls/)

---

## 📂 Project Structure

```
swe1-app/
│── mysite/          # Django project settings and URLs
│── polls/           # Polls app with models, views, templates
│── manage.py        # Django project management script
│── requirements.txt # Python dependencies
│── .ebextensions/   # Elastic Beanstalk configuration
```

---

## ⚡ Running Locally

Clone the repo:

```bash
git clone https://github.com/SamKh5/django-polls-app.git
cd django-polls-app
```

Create & activate virtual environment:

```bash
# Linux/Mac
python -m venv venv
source venv/bin/activate

# Windows
python -m venv venv
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run migrations:

```bash
python manage.py migrate
```

Start the dev server:

```bash
python manage.py runserver
```

---

## 🛠 Features

- Create polls with multiple choices  
- Vote in real time  
- View poll results instantly  
- Styled frontend with static CSS  

---

## 📜 License

This project is for **educational/demo purposes** only.  
