# Python core & Django generics
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.views import View
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
from django.shortcuts import redirect
from django.urls import reverse


# Models
from resume_builder.models import (
    Resume, WorkExperience, Education, Project, Certification,
    Award, Language, TechnicalSkill
)



# Forms
from resume_builder.forms import (
    WorkExperienceForm, EducationForm, ProjectForm,
    CertificationForm, AwardForm, LanguageForm, TechnicalSkillForm
)



class WorkExperienceListView(LoginRequiredMixin, ListView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_list.html'
    context_object_name = 'experiences'

    def get_queryset(self):
        return WorkExperience.objects.filter(resume__user=self.request.user)

class WorkExperienceCreateView(LoginRequiredMixin, CreateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()
        print("Form is valid and redirecting...")  # Testing log

        action = self.request.POST.get('action')
        if action == 'next':
            return redirect('project_create', resume_id=self.resume_id)
        else:
            return redirect('work_experience_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context


class WorkExperienceUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = WorkExperience
    form_class = WorkExperienceForm
    template_name = 'resume_builder/work_experience/work_experience_form.html'
    success_url = reverse_lazy('work_experience_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class WorkExperienceDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_confirm_delete.html'
    success_url = reverse_lazy('work_experience_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class WorkExperienceDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = WorkExperience
    template_name = 'resume_builder/work_experience/work_experience_detail.html'
    context_object_name = 'experience'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class EducationListView(LoginRequiredMixin, ListView):
        model = Education
        template_name = 'resume_builder/education/education_list.html'
        context_object_name = 'educations'

        def get_queryset(self):
            return Education.objects.filter(resume__user=self.request.user)

class EducationCreateView(LoginRequiredMixin, CreateView):
    model = Education
    form_class = EducationForm
    template_name = 'resume_builder/education/education_form.html'

    def form_valid(self, form):
        resume_id = self.kwargs['resume_id']
        form.instance.resume_id = resume_id
        self.object = form.save()

        action = self.request.POST.get('action')
        if action == 'next':
            return redirect('work_experience_create', resume_id=resume_id)
        else:
            return redirect('education_list', resume_id=resume_id)  # Or use a section review screen

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.kwargs['resume_id']
        return context

    def get_success_url(self):
        # Not used anymore since form_valid handles redirect manually
        return reverse('work_experience_create', kwargs={'resume_id': self.object.resume.id})

class EducationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
        model = Education
        form_class = EducationForm
        template_name = 'resume_builder/education/education_form.html'
        success_url = reverse_lazy('education_list')

        def test_func(self):
            return self.get_object().resume.user == self.request.user

class EducationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
        model = Education
        template_name = 'resume_builder/education/education_confirm_delete.html'
        success_url = reverse_lazy('education_list')

        def test_func(self):
            return self.get_object().resume.user == self.request.user

class EducationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
        model = Education
        template_name = 'resume_builder/education/education_detail.html'
        context_object_name = 'education'

        def test_func(self):
            return self.get_object().resume.user == self.request.user

# ----------- Project Views ------------
class ProjectListView(LoginRequiredMixin, ListView):
    model = Project
    template_name = 'resume_builder/project/project_list.html'
    context_object_name = 'projects'

    def get_queryset(self):
        return Project.objects.filter(resume__user=self.request.user)

class ProjectCreateView(LoginRequiredMixin, CreateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()

        action = self.request.POST.get('action')
        if action == 'next':
            return redirect('technicalskill_create', resume_id=self.resume_id)  # or whichever is your next step
        else:
            return redirect('project_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context

class ProjectUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Project
    form_class = ProjectForm
    template_name = 'resume_builder/project/project_form.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ProjectDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Project
    template_name = 'resume_builder/project/project_confirm_delete.html'
    success_url = reverse_lazy('project_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class ProjectDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Project
    template_name = 'resume_builder/project/project_detail.html'
    context_object_name = 'project'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# ----------- Certification Views ------------
class CertificationListView(LoginRequiredMixin, ListView):
    model = Certification
    template_name = 'resume_builder/certification/certification_list.html'
    context_object_name = 'certifications'

    def get_queryset(self):
        return Certification.objects.filter(resume__user=self.request.user)

class CertificationCreateView(LoginRequiredMixin, CreateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()

        action = self.request.POST.get("action")
        if action == "next":
            return redirect('award_create', resume_id=self.resume_id)
        return redirect('certification_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context

class CertificationUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Certification
    form_class = CertificationForm
    template_name = 'resume_builder/certification/certification_form.html'
    success_url = reverse_lazy('certification_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class CertificationDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Certification
    template_name = 'resume_builder/certification/certification_confirm_delete.html'
    success_url = reverse_lazy('certification_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class CertificationDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Certification
    template_name = 'resume_builder/certification/certification_detail.html'
    context_object_name = 'certification'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# ----------- Award Views ------------
class AwardListView(LoginRequiredMixin, ListView):
    model = Award
    template_name = 'resume_builder/award/award_list.html'
    context_object_name = 'awards'

    def get_queryset(self):
        return Award.objects.filter(resume__user=self.request.user)

class AwardCreateView(LoginRequiredMixin, CreateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()

        action = self.request.POST.get("action")
        if action == "next":
            return redirect('language_create', resume_id=self.resume_id)  # Next stop: Languages!
        return redirect('award_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context

class AwardUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Award
    form_class = AwardForm
    template_name = 'resume_builder/award/award_form.html'
    success_url = reverse_lazy('award_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class AwardDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Award
    template_name = 'resume_builder/award/award_confirm_delete.html'
    success_url = reverse_lazy('award_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class AwardDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Award
    template_name = 'resume_builder/award/award_detail.html'
    context_object_name = 'award'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# ----------- Language Views ------------
class LanguageListView(LoginRequiredMixin, ListView):
    model = Language
    template_name = 'resume_builder/language/language_list.html'
    context_object_name = 'languages'

    def get_queryset(self):
        return Language.objects.filter(resume__user=self.request.user)


class LanguageCreateView(LoginRequiredMixin, CreateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()

        action = self.request.POST.get("action")

        if action == "next":
            # ✅ Clean, correct redirect to detail view
            return redirect('resume_final_review', resume_id=self.resume_id)

        # Default redirect back to language list
        return redirect('language_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context


class LanguageUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Language
    form_class = LanguageForm
    template_name = 'resume_builder/language/language_form.html'
    success_url = reverse_lazy('language_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class LanguageDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Language
    template_name = 'resume_builder/language/language_confirm_delete.html'
    success_url = reverse_lazy('language_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class LanguageDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = Language
    template_name = 'resume_builder/language/language_detail.html'
    context_object_name = 'language'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

# ----------- Technical Skill Views ------------
class TechnicalSkillListView(LoginRequiredMixin, ListView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_list.html'
    context_object_name = 'technicalskills'

    def get_queryset(self):
        return TechnicalSkill.objects.filter(resume__user=self.request.user)

class TechnicalSkillCreateView(LoginRequiredMixin, CreateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technicalskill/technicalskill_form.html'

    def dispatch(self, request, *args, **kwargs):
        self.resume_id = self.kwargs.get('resume_id')
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        resume = get_object_or_404(Resume, id=self.resume_id, user=self.request.user)
        form.instance.resume = resume
        self.object = form.save()

        action = self.request.POST.get("action")
        if action == "next":
            return redirect('certification_create', resume_id=self.resume_id)  # or wherever the user should go next
        return redirect('technicalskill_list', resume_id=self.resume_id)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['resume_id'] = self.resume_id
        return context

class TechnicalSkillUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = TechnicalSkill
    form_class = TechnicalSkillForm
    template_name = 'resume_builder/technicalskill/technicalskill_form.html'
    success_url = reverse_lazy('technicalskill_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class TechnicalSkillDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_confirm_delete.html'
    success_url = reverse_lazy('technicalskill_list')

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class TechnicalSkillDetailView(LoginRequiredMixin, UserPassesTestMixin, DetailView):
    model = TechnicalSkill
    template_name = 'resume_builder/technicalskill/technicalskill_detail.html'
    context_object_name = 'technicalskill'

    def test_func(self):
        return self.get_object().resume.user == self.request.user

class TemplateSelectView(LoginRequiredMixin, UpdateView):
    model = Resume
    fields = ['template']
    template_name = 'resume_builder/resume/select_template.html'
    success_url = reverse_lazy('resume_detail')  # Change to your actual detail or preview route

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

from django.views import View
from django.shortcuts import render
from resume_builder.models import ResumeTemplate

class TemplateChooseView(LoginRequiredMixin, View):
    def get(self, request):
        templates = ResumeTemplate.objects.all()
        return render(request, 'resume_builder/resume/select_before_create.html', {'templates': templates})
class ResumeDownloadView(LoginRequiredMixin, View):
    def get(self, request, pk):
        return self._generate_pdf(request, pk)

    def post(self, request, pk):
        return self._generate_pdf(request, pk)

    def _generate_pdf(self, request, pk):
        resume = get_object_or_404(Resume, pk=pk, user=request.user)

        # Use default fallback if template is missing
        template_key = resume.template.format_type.lower() if resume.template else 'default'

        # ✅ Add complete context
        context = {
            'resume': resume,
            'educations': resume.educations.all(),
            'experiences': resume.work_experiences.all(),
            'projects': resume.projects.all(),
            'certifications': resume.certifications.all(),
            'skills': resume.technical_skills.all(),
            'awards': resume.awards.all(),
            'languages': resume.languages.all()
        }

        html_string = render_to_string(
            f'resume_templates/{template_key}.html',
            context
        )

        pdf = HTML(string=html_string).write_pdf()

        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = f'attachment; filename="{resume.slug}.pdf"'
        return response

class ResumeDetailView(LoginRequiredMixin, DetailView):
    model = Resume
    template_name = 'resume_builder/resume/detail.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'  # ✅ This line is crucial!

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = self.object

        context['educations'] = resume.educations.all()
        context['experiences'] = resume.work_experiences.all()
        context['projects'] = resume.projects.all()
        context['certifications'] = resume.certifications.all()
        context['skills'] = resume.technical_skills.all()
        context['awards'] = resume.awards.all()
        context['languages'] = resume.languages.all()

        return context


class ResumeListView(LoginRequiredMixin, ListView):
    model = Resume
    template_name = 'resume_builder/resume/list.html'
    context_object_name = 'resumes'

    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

class ResumeCreateView(LoginRequiredMixin, CreateView):
    model = Resume
    template_name = 'resume_builder/resume/create_resume.html'
    fields = ['title', 'summary']  # ⛔ Removed 'template' to hide it from UI
    success_url = reverse_lazy('resume_list')

    def get_initial(self):
        initial = super().get_initial()
        template_id = self.request.GET.get('template')
        if template_id:
            initial['template'] = template_id
        return initial

    def form_valid(self, form):
        form.instance.user = self.request.user
        form.instance.template_id = self.request.GET.get('template')
        self.object = form.save()

        return redirect(reverse('education_create', kwargs={'resume_id': self.object.pk}))


class ResumeFinalReviewView(LoginRequiredMixin, DetailView):
    model = Resume
    template_name = 'resume_builder/resume/final_review.html'
    context_object_name = 'resume'
    pk_url_kwarg = 'resume_id'  # ✅ This tells Django to use resume_id instead of pk

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        resume = self.object
        context['educations'] = resume.educations.all()
        context['experiences'] = resume.work_experiences.all()
        context['projects'] = resume.projects.all()
        context['certifications'] = resume.certifications.all()
        context['skills'] = resume.technical_skills.all()
        context['awards'] = resume.awards.all()
        context['languages'] = resume.languages.all()
        return context

class ResumeEditView(LoginRequiredMixin, UpdateView):
    model = Resume
    template_name = 'resume_builder/resume/edit.html'
    context_object_name = 'resume'
    fields = ['title', 'summary', 'template']

    # Use 'resume_id' from URL instead of default 'pk'
    pk_url_kwarg = 'resume_id'

    # Limit queryset to resumes owned by the logged-in user
    def get_queryset(self):
        return Resume.objects.filter(user=self.request.user)

    # Optional: customize success logic
    def form_valid(self, form):
        response = super().form_valid(form)
        # You can add a message here using Django's messages framework if desired
        return response

    # Where to redirect after saving the resume
    success_url = reverse_lazy('resume_list')
