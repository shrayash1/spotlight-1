from calendar import c
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.db.models import F
from project.forms import CreateProjectForm
from project.models import Project


# Create your views here.
class HomeView(ListView):
    model = Project
    template_name = 'home.html'
    context_object_name = 'project'

    def get(self, *args, **kwargs):
        str = self.kwargs.get("str")
        if str:
            search_result = Project.objects.filter(category__title__iexact=str)[:9]
            self.object_list = search_result
            context = self.get_context_data()
        else:
            self.object_list = Project.objects.all()[:9]
            context = self.get_context_data()
        return self.render_to_response(context)
        

class AboutUs(TemplateView):
    template_name = 'our_team.html'


class CreateProject(CreateView):
    form_class = CreateProjectForm
    template_name = 'project/create.html'
    success_url = reverse_lazy('profile')

    def form_valid(self, form):
        if self.request.user.is_authenticated:
            project = form.save(commit=False)
            project.creator = self.request.user
            project.save()
            return super().form_valid(form)
        else:
            return super().form_invalid(form)
       

class ViewProjects(TemplateView):
    template_name = 'project/view_all_projects.html'


class ProjectDetailView(DetailView):
    model = Project
    template_name = 'project/view-project-details.html'
    context_object_name = 'project'
    pk_url_kwarg = 'id'

    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        context['projects'] = self.model.objects.all()[:3]
        return context
    
    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        self.object.views=F('views')+1
        self.object.save()
        self.object.refresh_from_db()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
class ProfileView(TemplateView):
    template_name = 'profile.html'
