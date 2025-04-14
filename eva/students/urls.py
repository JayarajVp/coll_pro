from django.urls import path
from . import views
from .views import login_view

urlpatterns = [
    path("", login_view, name="login"),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("logout/", views.logout_view, name="logout"),
    path("host-event/", views.host_event, name="host_event"),
    path("submit-event/", views.submit_event, name="submit_event"),  # Make sure submit_event is included
    path("view-event/", views.view_event, name="view_event"),
    path("raise-complaint/", views.raise_complaint, name="raise_complaint"),
    path("view-complaint/", views.view_complaint, name="view_complaint"),
    path("submit-complaint/", views.submit_complaint, name="submit_complaint"),
    path("view-event/", views.view_event, name="view_event"),
    path("view-complaint/", views.view_complaint, name="view_complaint"),

]
