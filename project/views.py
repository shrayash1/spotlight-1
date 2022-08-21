from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView

from project.forms import CreateProjectForm
from project.models import Project


# Create your views here.
class HomeView(TemplateView):
    template_name = 'home.html'
    
class AboutUs(TemplateView):
    template_name = 'our_team.html'
    
class CreateProject(CreateView):
    form_class = CreateProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('profile')
    
    def form_valid(self, form):
        project = form.save(commit=False)
        project.creator = self.request.user
        project.save()
        return super().form_valid(form)

class ViewProjects(TemplateView):
    template_name = 'project/view_all_projects.html'

class ViewProjectDetail(TemplateView):
    template_name = 'project/view-project-details.html'