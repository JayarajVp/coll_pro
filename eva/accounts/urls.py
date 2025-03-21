from django.urls import path
from .views import login_view, dashboard, logout_view, host_event, view_event, raise_complaint, view_complaint

urlpatterns = [
    path("", login_view, name="login"),
    path("dashboard/", dashboard, name="dashboard"),
    path("logout/", logout_view, name="logout"),
    path("host-event/", host_event, name="host_event"),
    path("view-event/", view_event, name="view_event"),
    path("raise-complaint/", raise_complaint, name="raise_complaint"),
    path("view-complaint/", view_complaint, name="view_complaint"),
]
