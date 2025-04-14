from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),

    # Routes for selecting role
    path('select/student/', views.redirect_to_students, name='select_student'),
    path('select/teacher/', views.redirect_to_teachers, name='select_teacher'),

    # Students module handles URLs like /std/login, /std/dashboard, etc.
    path('std/', include('students.urls')),

    # Teacher or shared login/logout/dashboard handled at root level
    path('', include('accounts.urls')),
]
