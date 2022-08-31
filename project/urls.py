from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('home/<str:str>', HomeView.as_view(), name='home'),
    path('about-us/', AboutUs.as_view(), name='about-us'),
    path('create-project/', CreateProject.as_view(), name='create-project'),
    path('view-projects/', ViewProjects.as_view(), name='view-projects'),
    path('project-detail/<int:id>', ProjectDetailView.as_view(), name='project-detail'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
