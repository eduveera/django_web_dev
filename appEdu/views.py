from django.shortcuts import render

# Create your views here.
def home_view(request):
    context = {
        'message': 'Hello from myapp!',
    }
    return render(request, 'appEdu/home.html', context)