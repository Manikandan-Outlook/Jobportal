from django.contrib import admin
from .models import JobUser

class QuestionAdmin(admin.ModelAdmin):

    fields = ['name', 'resume_title', 'resume']

admin.site.register(JobUser, QuestionAdmin)
