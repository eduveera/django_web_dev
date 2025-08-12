from django.shortcuts import render, redirect
from .forms import StudentForm

def enquiry_view(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('thank_you')  # or whichever route handles success
    else:
        form = StudentForm()
    return render(request, 'appEdu/enquiry.html', {'form': form})
