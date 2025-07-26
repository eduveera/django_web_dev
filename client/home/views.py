from django.shortcuts import render
from django.core.mail import EmailMessage
from .models import Form
import threading
import re

def send_confirmation_email(email, name):
    try:
        msg = EmailMessage(
            subject="Form Submitted",
            body=f"<h2>Hello {name},</h2><p>Your form was submitted successfully!</p>",
            from_email="infoeduveera@gmail.com",
            to=[email]
        )
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        print("Email error:", e)

def is_valid_gmail(email):
    return re.match(r'^[a-zA-Z0-9_.+-]+@gmail\.com$', email)

def is_valid_indian_phone(phone):
    return re.match(r'^[6-9]\d{9}$', phone)

def index(request):
    courses = ['B-Tech', 'B.Com', 'MBA', 'BBA']  # dropdown values

    if request.method == 'POST':
        name = request.POST['name']
        age = request.POST['age']
        mobile_no = request.POST['mobile_no']
        email = request.POST['email']
        course = request.POST['course']

        # Age check
        if not age.isdigit() or int(age) <= 15:
            return render(request, 'home/home.html', {
                'error': "Age must be greater than 15.",
                'error_field': 'age',
                'courses': courses
            })

        if not is_valid_gmail(email):
            return render(request, 'home/home.html', {
                'error': "Please enter a valid Gmail address.",
                'error_field': 'email',
                'courses': courses
            })

        if not is_valid_indian_phone(mobile_no):
            return render(request, 'home/home.html', {
                'error': "Please enter a valid 10-digit Indian mobile number.",
                'error_field': 'mobile_no',
                'courses': courses
            })

        # Save to DB
        Form.objects.create(
            name=name,
            age=age,
            mobile_no=mobile_no,
            email=email,
            course=course
        )

        # Send email in background
        threading.Thread(target=send_confirmation_email, args=(email, name)).start()

        return render(request, 'home/home.html', {'success': True, 'courses': courses})

    return render(request, 'home/home.html', {'courses': ['B-Tech', 'B.Com', 'MBA', 'BBA']})
