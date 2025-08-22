# Education Consultancy Website

A Django-based web application where students submit educational consultancy forms—storing data in the backend, sending confirmation emails, and managing consultation status via a customized admin interface (built with Jazzmin). Frontend stack includes HTML, CSS, Tailwind, JavaScript, and Bootstrap.

---

##  Table of Contents

- [Built With](#built-with)  
- [Getting Started](#getting-started)  
- [Usage](#usage)  
- [Features](#features)  
- [Project Structure](#project-structure)  
- [Contributing](#contributing)  
- [License](#license)  
- [Contact](#contact)

---

##  Built With

- **Backend**: Django, Python, django-jazzmin  
- **Frontend**: HTML, CSS, Tailwind CSS, Bootstrap, JavaScript  
- **Email Handling**: Django’s `send_mail()` / `EmailMultiAlternatives`

---

##  Getting Started

### Prerequisites

- Python 3.8 or higher  
- Django 4.x or 5.x  
- Gmail SMTP or similar for email functionality

### Installation

```bash
git clone https://github.com/your-repo/education-consultancy.git
cd education-consultancy
python -m venv venv
source venv/bin/activate  # or .\\venv\\Scripts\\activate on Windows
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
