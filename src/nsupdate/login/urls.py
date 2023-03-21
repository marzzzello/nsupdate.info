# -*- coding: utf-8 -*-
from django.urls import path
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
)

urlpatterns = [
    # login and logout url
    path('login/', LoginView.as_view(template_name='login.html'), name='login'),
    # or use logout with template 'logout.html'
    path('logout/', LogoutView.as_view(), name='logout'),
    # password reset urls
    path('password_reset/', PasswordResetView.as_view(template_name='password_reset.html'), name='password_reset'),
    path(
        'password_reset_done/',
        PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done',
    ),
    path(
        'password_reset_confirm/<uidb64>/<token>/',
        PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm',
    ),
    path(
        'password_reset_complete/',
        PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete',
    ),
]
