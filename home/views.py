from django.shortcuts import render
from .models import Enquiry
from django.core.mail import EmailMessage
import threading

def send_email(name, email):
    try:
        msg = EmailMessage(
            subject="Thanks for registering!",
            body=f"<h2>Hello {name},</h2><p>Your registration has been received.</p>",
            from_email="mydatayatra@gmail.com",
            to=[email]
        )
        msg.content_subtype = "html"
        msg.send()
    except Exception as e:
        print("Email error:", e)

def index(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        dob = request.POST['dob']
        university = request.POST['university']
        course = request.POST['course']

        # Save to database
        Enquiry.objects.create(
            name=name,
            email=email,
            phone=phone,
            date_of_birth=dob,
            university=university,
            course=course,
        )

        # Send confirmation email
        threading.Thread(target=send_email, args=(name, email)).start()

        return render(request, 'home/home.html', {'success': True})

    return render(request, 'home/home.html')