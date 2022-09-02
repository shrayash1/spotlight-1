from django import forms

from project.models import Project


class CreateProjectForm(forms.ModelForm):
    deadline = forms.DateTimeField(label='Deadline date:', widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Project
        fields = '__all__'
        exclude = ['creator','created_date','views', 'favourite']