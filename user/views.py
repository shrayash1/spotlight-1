from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView
from django.views.generic.base import TemplateView

from project.models import Project
from .forms import SignUpForm
from .models import Profile
    
# Sign Up View
class SignUpView(CreateView):
    form_class = SignUpForm
    success_url = reverse_lazy('login')
    template_name = 'auth/register.html'
    
    def form_valid(self, form):
        self.object = form.save()
        role = form.cleaned_data.get('role')
        Profile.objects.create(user=self.object, role=role)
        return super().form_valid(form)

class UserLoginView(LoginView):
    def get_success_url(self) -> str:
        return reverse_lazy('profile')

        
class ProfileView(TemplateView):
    template_name = 'profile_new.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = Profile.objects.get(user=self.request.user)
        context['projects'] =  Project.objects.filter(creator = self.request.user)
        return context