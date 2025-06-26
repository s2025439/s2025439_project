from django import forms
from .models import (
    ResumeTemplate, Resume, ResumeSection, WorkExperience,
    TechnicalSkill, Education, Technology, Project,
    Certification, Award, Language
)

class ResumeTemplateForm(forms.ModelForm):
    class Meta:
        model = ResumeTemplate
        fields = ['name', 'description', 'format_type', 'version']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'format_type': forms.Select(attrs={'class': 'form-select'}),
            'version': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = ['title', 'slug', 'summary', 'tags', 'template', 'language', 'visibility']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'}),
            'summary': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'tags': forms.TextInput(attrs={'class': 'form-control'}),
            'template': forms.Select(attrs={'class': 'form-select'}),
            'language': forms.Select(attrs={'class': 'form-select'}),
            'visibility': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class ResumeSectionForm(forms.ModelForm):
    class Meta:
        model = ResumeSection
        fields = ['section_type', 'title', 'content', 'order', 'is_visible']
        widgets = {
            'section_type': forms.Select(attrs={'class': 'form-select'}),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'order': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class WorkExperienceForm(forms.ModelForm):
    class Meta:
        model = WorkExperience
        fields = ['job_title', 'company', 'location', 'start_date', 'end_date', 'is_current', 'description', 'achievements', 'technologies']
        widgets = {
            'job_title': forms.TextInput(attrs={'class': 'form-control'}),
            'company': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'is_current': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'achievements': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'technologies': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class TechnicalSkillForm(forms.ModelForm):
    class Meta:
        model = TechnicalSkill
        fields = ['technology', 'proficiency', 'years_experience', 'last_used', 'project_count', 'is_visible']
        widgets = {
            'technology': forms.Select(attrs={'class': 'form-select'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
            'years_experience': forms.NumberInput(attrs={'class': 'form-control'}),
            'last_used': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'project_count': forms.NumberInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class EducationForm(forms.ModelForm):
    class Meta:
        model = Education
        fields = ['degree', 'institution', 'location', 'start_date', 'end_date', 'gpa', 'description', 'is_visible']
        widgets = {
            'degree': forms.TextInput(attrs={'class': 'form-control'}),
            'institution': forms.TextInput(attrs={'class': 'form-control'}),
            'location': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'gpa': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class TechnologyForm(forms.ModelForm):
    class Meta:
        model = Technology
        fields = ['name', 'category', 'icon']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'icon': forms.TextInput(attrs={'class': 'form-control'}),
        }

class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'role', 'start_date', 'end_date', 'description', 'technologies', 'outcomes', 'url', 'is_active']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'role': forms.TextInput(attrs={'class': 'form-control'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'technologies': forms.SelectMultiple(attrs={'class': 'form-select'}),
            'outcomes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'url': forms.URLInput(attrs={'class': 'form-control'}),
            'is_active': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class CertificationForm(forms.ModelForm):
    class Meta:
        model = Certification
        fields = ['name', 'issuer', 'issue_date', 'expiration_date', 'credential_id', 'verification_url', 'skills']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'expiration_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'credential_id': forms.TextInput(attrs={'class': 'form-control'}),
            'verification_url': forms.URLInput(attrs={'class': 'form-control'}),
            'skills': forms.SelectMultiple(attrs={'class': 'form-select'}),
        }

class AwardForm(forms.ModelForm):
    class Meta:
        model = Award
        fields = ['title', 'issuer', 'issue_date', 'category', 'description', 'impact_metrics', 'is_visible']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'issuer': forms.TextInput(attrs={'class': 'form-control'}),
            'issue_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-select'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'impact_metrics': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }

class LanguageForm(forms.ModelForm):
    class Meta:
        model = Language
        fields = ['name', 'proficiency', 'certification', 'is_visible']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'proficiency': forms.Select(attrs={'class': 'form-select'}),
            'certification': forms.TextInput(attrs={'class': 'form-control'}),
            'is_visible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }