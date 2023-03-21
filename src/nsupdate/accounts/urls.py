from django.urls import path, re_path
from django.views.generic.base import TemplateView

from registration.backends.default.views import ActivationView
from registration.backends.default.views import RegistrationView

from .views import UserProfileView, DeleteUserView, UserChangePasswordView


urlpatterns = [
    path('profile/', UserProfileView.as_view(), name="account_profile"),
    path('settings/', UserChangePasswordView.as_view(), name='account_settings'),
    path('delete/', DeleteUserView.as_view(), name="account_delete"),
    # registration start
    path(
        'activate/complete/',
        TemplateView.as_view(template_name='registration/activation_complete.html'),
        name='registration_activation_complete',
    ),
    # Activation keys get matched by \w+ instead of the more specific
    # [a-fA-F0-9]{40} because a bad activation key should still get to the view;
    # that way it can return a sensible "invalid key" message instead of a
    # confusing 404.
    re_path(r'^activate/(?P<activation_key>\w+)/$', ActivationView.as_view(), name='registration_activate'),
    path('register/', RegistrationView.as_view(), name='registration_register'),
    path(
        'register/complete/',
        TemplateView.as_view(template_name='registration/registration_complete.html'),
        name='registration_complete',
    ),
    path(
        'register/closed/',
        TemplateView.as_view(template_name='registration/registration_closed.html'),
        name='registration_disallowed',
    ),
    # registration end
]
