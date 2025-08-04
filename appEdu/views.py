from django.shortcuts import render, redirect
from .forms import StudentForm


# Create your views here.
def home_view(request):
    context = {
        'message': 'Hello from myapp!',
    }
    return render(request, 'appEdu/home.html', context)


def student_signup(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # or show a success message
    else:
        form = StudentForm()
    return render(request, 'students/signup.html', {'form': form})
