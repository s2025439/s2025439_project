from django.contrib import admin
from .models import Resume, ResumeTemplate, ResumeSection  # include others if needed

admin.site.register(Resume)
admin.site.register(ResumeTemplate)
admin.site.register(ResumeSection)