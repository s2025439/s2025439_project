from django.urls import path
from .views import ResumeCreateView

from .views import (
    WorkExperienceListView, WorkExperienceCreateView, WorkExperienceUpdateView,
    WorkExperienceDeleteView, WorkExperienceDetailView,
    EducationListView, EducationCreateView, EducationUpdateView,
    EducationDeleteView, EducationDetailView,
    ProjectListView, ProjectCreateView, ProjectUpdateView,
    ProjectDeleteView, ProjectDetailView,
    CertificationListView, CertificationCreateView, CertificationUpdateView,
    CertificationDeleteView, CertificationDetailView,
    AwardListView, AwardCreateView, AwardUpdateView,
    AwardDeleteView, AwardDetailView,
    LanguageListView, LanguageCreateView, LanguageUpdateView,
    LanguageDeleteView, LanguageDetailView,
    TechnicalSkillListView, TechnicalSkillCreateView, TechnicalSkillUpdateView,
    TechnicalSkillDeleteView, TechnicalSkillDetailView,
)
from .views import (
    TemplateSelectView, ResumeDownloadView,
    ResumeDetailView, ResumeListView,TemplateChooseView,  # 👈 Add these
)

urlpatterns = [

# Resume actions
    path('resume/<int:pk>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('resume/', ResumeListView.as_view(), name='resume_list'),
    path('resume/select-template/', TemplateChooseView.as_view(), name='resume_template_select'),

    # Resume actions
    path('resume/<int:pk>/select-template/', TemplateSelectView.as_view(), name='resume_select_template'),
    path('resume/<int:pk>/download/', ResumeDownloadView.as_view(), name='resume_download'),
    path('resume/create/', ResumeCreateView.as_view(), name='resume_create'),


    # Work Experience URLs
    path('work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),

    # Education URLs
    path('resume/<int:resume_id>/section/education/', EducationListView.as_view(), name='education_list'),
    path('resume/<int:resume_id>/section/education/add/', EducationCreateView.as_view(), name='education_create'),
    path('resume/<int:resume_id>/section/education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('resume/<int:resume_id>/section/education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    path('resume/<int:resume_id>/section/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),

    # Project URLs
    path('projects/', ProjectListView.as_view(), name='project_list'),
    path('projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # Certification URLs
    path('certifications/', CertificationListView.as_view(), name='certification_list'),
    path('certifications/add/', CertificationCreateView.as_view(), name='certification_create'),
    path('certifications/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('certifications/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    path('certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),

    # Award URLs
    path('awards/', AwardListView.as_view(), name='award_list'),
    path('awards/add/', AwardCreateView.as_view(), name='award_create'),
    path('awards/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('awards/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('awards/<int:pk>/', AwardDetailView.as_view(), name='award_detail'),

    # Language URLs
    path('languages/', LanguageListView.as_view(), name='language_list'),
    path('languages/add/', LanguageCreateView.as_view(), name='language_create'),
    path('languages/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('languages/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('languages/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    # Technical Skill URLs
    path('technical-skills/', TechnicalSkillListView.as_view(), name='technicalskill_list'),
    path('technical-skills/add/', TechnicalSkillCreateView.as_view(), name='technicalskill_create'),
    path('technical-skills/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technicalskill_update'),
    path('technical-skills/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technicalskill_delete'),
    path('technical-skills/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technicalskill_detail'),
]