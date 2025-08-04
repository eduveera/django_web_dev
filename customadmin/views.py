from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from datetime import timedelta
from django.utils import timezone

def admin_login(request):
    try:
        if request.user.is_authenticated:
            return redirect('dashboard')

        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            if not User.objects.filter(username=username).exists():
                messages.info(request, 'Account not found')
                return redirect(request.META.get('HTTP_REFERER', '/'))

            user = authenticate(request, username=username, password=password)
            if user is not None and user.is_superuser:
                login(request, user)
                return redirect('dashboard')


            messages.info(request, 'Invalid credentials or not an admin')
            return redirect(request.META.get('HTTP_REFERER', '/'))

        return render(request, 'login.html')

    except Exception as e:
        print(e)
        messages.error(request, 'An unexpected error occurred')
        return redirect('/')

def dashboard(request):
    total_users = User.objects.count()
    new_signups = User.objects.filter(date_joined__gte=timezone.now() - timedelta(days=7)).count()
    active_sessions = 0  # Optional: can add later using session model

    # Example static activity data (replace with your logic or DB)
    recent_activities = [
        {'user': 'admin', 'description': 'Logged in', 'timestamp': '2025-08-03 12:00'},
        {'user': 'vicky', 'description': 'Added a student', 'timestamp': '2025-08-02 16:45'},
    ]

    return render(request, 'dashboard.html', {
        'total_users': total_users,
        'new_signups': new_signups,
        'active_sessions': active_sessions,
        'recent_activities': recent_activities,
    })

def admin_logout(request):
    logout(request)
    return redirect('admin_login')  