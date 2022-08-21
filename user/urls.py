from sre_constants import SUCCESS
from django.urls import path
from .views import *
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('signup/', SignUpView.as_view(),
         name='signup'),
    path('profile/', ProfileView.as_view(),
         name='profile'),
    path('login/',
         auth_views.LoginView.as_view(
             template_name='auth/login.html'),
         name='login'),
    path('accounts/logout/',
         auth_views.LogoutView.as_view(),
         name='logout'),
    path('accounts/changepassword/',
         auth_views.PasswordChangeView.as_view(
             template_name='auth/change_password.html',),
         name='changepass'),
    path('accounts/password/reset/',
         auth_views.PasswordResetView.as_view(
             template_name='auth/reset_password.html'),
         name='password-reset'),
    path('password/reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='auth/password_reset_done.html'),
         name='password_reset_done'),
    path('password/reset/confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='auth/password_reset_confirm.html'),
         name='password_reset_confirm'),
    path('password/reset/complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='auth/password_reset_complete.html'),
         name='password_reset_complete'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
