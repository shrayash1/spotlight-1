from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.views.generic.base import TemplateView
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


class ProfileView(TemplateView):
    template_name = 'profile.html'