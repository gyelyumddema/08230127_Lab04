from django.contrib import admin
from .models import LearningJourney, AboutMe, ProjectDocumentation

# Register your models here.
@admin.register(LearningJourney)
class LearningJourneyAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_learned']
    list_filter = ['date_learned']

@admin.register(AboutMe)
class AboutMeAdmin(admin.ModelAdmin):
    list_display = ['name', 'student_id', 'email']


@admin.register(ProjectDocumentation)
class ProjectDocumentationAdmin(admin.ModelAdmin):
    list_display = ['title', 'image']