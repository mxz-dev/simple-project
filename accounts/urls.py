from django.urls import path, reverse_lazy
from django.contrib.auth.views import (
    PasswordResetView, 
    PasswordResetDoneView, 
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from . import views

app_name = "accounts"

urlpatterns = [
    path("auth/login/", views.login_view , name="login" ),
    path("user/logout/", views.logout_view , name="logout"),
    path("auth/register/", views.registration_view , name="register"),
    path("user/reset-password/" , PasswordResetView.as_view(template_name="accounts/auth/password_reset_form.html", success_url=reverse_lazy("accounts:password_reset_done")) , name="password_reset"),
    path("user/reset-password/done/" , PasswordResetDoneView.as_view(template_name="accounts/auth/password_reset_done.html") , name="password_reset_done"),
    path("user/reset-password-confirm/<uidb64>/<token>/" , PasswordResetConfirmView.as_view(template_name="accounts/auth/password_reset_confirm.html", success_url=reverse_lazy("accounts:password_reset_complete")) , name="password_reset_confirm"),
    path("user/reset-password-complete/" , PasswordResetCompleteView.as_view(template_name="accounts/auth/password_reset_complete.html") , name="password_reset_complete"),

]
