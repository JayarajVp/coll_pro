from django.shortcuts import render, redirect

def home(request):
    return render(request, 'home.html')

def redirect_to_students(request):
    return redirect('/std/login')  # or appropriate URL

def redirect_to_teachers(request):
    return redirect('/login')  # or appropriate URL for teachers
