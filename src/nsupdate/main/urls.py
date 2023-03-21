"""
main app url dispatching
"""

from django.urls import path

from .views import (
    HomeView,
    OverviewView,
    HostView,
    AddHostView,
    DeleteHostView,
    AboutView,
    GenerateSecretView,
    GenerateNSSecretView,
    RobotsTxtView,
    DomainView,
    AddDomainView,
    DeleteDomainView,
    StatusView,
    JsUpdateView,
    UpdaterHostConfigOverviewView,
    UpdaterHostConfigView,
    DeleteUpdaterHostConfigView,
    RelatedHostOverviewView,
    RelatedHostView,
    AddRelatedHostView,
    DeleteRelatedHostView,
    CustomTemplateView,
)
from ..api.views import (
    myip_view,
    DetectIpView,
    AjaxGetIps,
    NicUpdateView,
    AuthorizedNicUpdateView,
    NicDeleteView,
    AuthorizedNicDeleteView,
)


urlpatterns = [
    # interactive web ui
    path('', HomeView.as_view(), name="home"),
    path('about/', AboutView.as_view(), name="about"),
    path('custom/<str:template>/', CustomTemplateView.as_view(), name="custom"),
    path('update', JsUpdateView.as_view(), name='update'),
    path('overview/', OverviewView.as_view(), name='overview'),
    path('status/', StatusView.as_view(), name='status'),
    path('generate_secret/<int:pk>/', GenerateSecretView.as_view(), name='generate_secret_view'),
    path('generate_ns_secret/<int:pk>/', GenerateNSSecretView.as_view(), name='generate_ns_secret_view'),
    path('host/<int:pk>/', HostView.as_view(), name='host_view'),
    path('host/add/', AddHostView.as_view(), name='add_host'),
    path('host/<int:pk>/delete/', DeleteHostView.as_view(), name='delete_host'),
    path('host/<int:mpk>/related/', RelatedHostOverviewView.as_view(), name='related_host_overview'),
    path('host/<int:mpk>/related/<int:pk>/', RelatedHostView.as_view(), name='related_host_view'),
    path('host/<int:mpk>/related/add/', AddRelatedHostView.as_view(), name='add_related_host'),
    path('host/<int:mpk>/related/<int:pk>/delete/', DeleteRelatedHostView.as_view(), name='delete_related_host'),
    path('domain/<int:pk>/', DomainView.as_view(), name='domain_view'),
    path('domain/add/', AddDomainView.as_view(), name='add_domain'),
    path('domain/<int:pk>/delete/', DeleteDomainView.as_view(), name='delete_domain'),
    path(
        'updater_hostconfig_overview/<int:pk>/',
        UpdaterHostConfigOverviewView.as_view(),
        name='updater_hostconfig_overview',
    ),
    path('updater_hostconfig/<int:pk>/', UpdaterHostConfigView.as_view(), name='updater_hostconfig'),
    path(
        'updater_hostconfig/<int:pk>/delete/', DeleteUpdaterHostConfigView.as_view(), name='delete_updater_hostconfig'
    ),
    # internal use by the web ui
    path('detectip/<str:sessionid>/', DetectIpView.as_view(), name='detectip'),
    path('ajax_get_ips/', AjaxGetIps.as_view(), name="ajax_get_ips"),
    path('nic/update_authorized/', AuthorizedNicUpdateView.as_view(), name='nic_update_authorized'),
    path('nic/delete_authorized/', AuthorizedNicDeleteView.as_view(), name='nic_delete_authorized'),
    # api (for update clients)
    path('myip/', myip_view, name='myip'),
    path('nic/update/', NicUpdateView.as_view(), name='nic_update'),
    path('nic/delete/', NicDeleteView.as_view(), name='nic_delete'),
    path('robots.txt', RobotsTxtView.as_view(), name='robots'),
]
