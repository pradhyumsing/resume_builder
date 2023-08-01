

from django.shortcuts import render, redirect
from .models import Resume
from .forms import ResumeForm

def create_resume(request):
    if request.method == 'POST':
        form = ResumeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('resume_display')
    else:
        form = ResumeForm()
    return render(request, 'create_resume.html', {'form': form})

def display_resume(request):
    resume = Resume.objects.last()  # Get the most recent resume for display
    return render(request, 'display_resume.html', {'resume': resume})
