from django.urls import path
from .views import (
    ResumeCreateView, ResumeEditView, TemplateChooseView, ResumeDetailView,
    ResumeListView, TemplateSelectView, ResumeDownloadView,
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
    TechnicalSkillDeleteView, TechnicalSkillDetailView,ResumeFinalReviewView,
)

urlpatterns = [
    # Resume actions
    path('resume/', ResumeListView.as_view(), name='resume_list'),
    path('resume/<int:resume_id>/review/', ResumeFinalReviewView.as_view(), name='resume_final_review'),
    path('web/resume/<int:resume_id>/', ResumeDetailView.as_view(), name='resume_detail'),
    path('web/resume/<int:resume_id>/edit/', ResumeEditView.as_view(), name='resume_edit'),
    path('resume/select-template/', TemplateChooseView.as_view(), name='resume_template_select'),
    path('resume/<int:pk>/select-template/', TemplateSelectView.as_view(), name='resume_select_template'),
    path('resume/<int:pk>/download/', ResumeDownloadView.as_view(), name='resume_download'),
    path('resume/create/', ResumeCreateView.as_view(), name='resume_create'),

    # Work Experience URLs
    path('resume/<int:resume_id>/work-experience/', WorkExperienceListView.as_view(), name='work_experience_list'),
    path('resume/<int:resume_id>/work-experience/add/', WorkExperienceCreateView.as_view(), name='work_experience_create'),
    path('resume/<int:resume_id>/work-experience/<int:pk>/edit/', WorkExperienceUpdateView.as_view(), name='work_experience_update'),
    path('resume/<int:resume_id>/work-experience/<int:pk>/delete/', WorkExperienceDeleteView.as_view(), name='work_experience_delete'),
    path('resume/<int:resume_id>/work-experience/<int:pk>/', WorkExperienceDetailView.as_view(), name='work_experience_detail'),

    # Education URLs
    path('resume/<int:resume_id>/section/education/', EducationListView.as_view(), name='education_list'),
    path('resume/<int:resume_id>/section/education/add/', EducationCreateView.as_view(), name='education_create'),
    path('resume/<int:resume_id>/section/education/<int:pk>/edit/', EducationUpdateView.as_view(), name='education_update'),
    path('resume/<int:resume_id>/section/education/<int:pk>/delete/', EducationDeleteView.as_view(), name='education_delete'),
    path('resume/<int:resume_id>/section/education/<int:pk>/', EducationDetailView.as_view(), name='education_detail'),

    # Project URLs
    path('resume/<int:resume_id>/section/projects/', ProjectListView.as_view(), name='project_list'),
    path('resume/<int:resume_id>/section/projects/add/', ProjectCreateView.as_view(), name='project_create'),
    path('resume/<int:resume_id>/section/projects/<int:pk>/edit/', ProjectUpdateView.as_view(), name='project_update'),
    path('resume/<int:resume_id>/section/projects/<int:pk>/delete/', ProjectDeleteView.as_view(), name='project_delete'),
    path('resume/<int:resume_id>/section/projects/<int:pk>/', ProjectDetailView.as_view(), name='project_detail'),

    # Certification URLs
    path('resume/<int:resume_id>/section/certifications/', CertificationListView.as_view(), name='certification_list'),
    path('resume/<int:resume_id>/section/certifications/add/', CertificationCreateView.as_view(), name='certification_create'),
    path('resume/<int:resume_id>/section/certifications/<int:pk>/edit/', CertificationUpdateView.as_view(), name='certification_update'),
    path('resume/<int:resume_id>/section/certifications/<int:pk>/delete/', CertificationDeleteView.as_view(), name='certification_delete'),
    path('resume/<int:resume_id>/section/certifications/<int:pk>/', CertificationDetailView.as_view(), name='certification_detail'),

    # Award URLs
    path('resume/<int:resume_id>/section/awards/', AwardListView.as_view(), name='award_list'),
    path('resume/<int:resume_id>/section/awards/add/', AwardCreateView.as_view(), name='award_create'),
    path('resume/<int:resume_id>/section/awards/<int:pk>/edit/', AwardUpdateView.as_view(), name='award_update'),
    path('resume/<int:resume_id>/section/awards/<int:pk>/delete/', AwardDeleteView.as_view(), name='award_delete'),
    path('resume/<int:resume_id>/section/awards/<int:pk>/', AwardDetailView.as_view(), name='award_detail'),

    # Language URLs
    path('resume/<int:resume_id>/section/languages/', LanguageListView.as_view(), name='language_list'),
    path('resume/<int:resume_id>/section/languages/add/', LanguageCreateView.as_view(), name='language_create'),
    path('resume/<int:resume_id>/section/languages/<int:pk>/edit/', LanguageUpdateView.as_view(), name='language_update'),
    path('resume/<int:resume_id>/section/languages/<int:pk>/delete/', LanguageDeleteView.as_view(), name='language_delete'),
    path('resume/<int:resume_id>/section/languages/<int:pk>/', LanguageDetailView.as_view(), name='language_detail'),

    # Technical Skill URLs
    path('resume/<int:resume_id>/section/technical-skills/', TechnicalSkillListView.as_view(), name='technicalskill_list'),
    path('resume/<int:resume_id>/section/technical-skills/add/', TechnicalSkillCreateView.as_view(), name='technicalskill_create'),
    path('resume/<int:resume_id>/section/technical-skills/<int:pk>/edit/', TechnicalSkillUpdateView.as_view(), name='technicalskill_update'),
    path('resume/<int:resume_id>/section/technical-skills/<int:pk>/delete/', TechnicalSkillDeleteView.as_view(), name='technicalskill_delete'),
    path('resume/<int:resume_id>/section/technical-skills/<int:pk>/', TechnicalSkillDetailView.as_view(), name='technicalskill_detail'),
]