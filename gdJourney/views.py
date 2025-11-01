from django.shortcuts import render
from .models import LearningJourney, AboutMe, ProjectDocumentation

# Create your views here.
def index(request):
    """Home page displaying learning journey"""
    learnings = LearningJourney.objects.all().order_by('-date_learned')
    documentation = ProjectDocumentation.objects.all()
    return render(request, 'index.html', {'learnings': learnings, 'documentation': documentation})

def about_me(request):
    """About me page"""
    about_info = AboutMe.objects.first()  # Get first AboutMe entry
    return render(request, 'aboutMe.html', {'about': about_info})
