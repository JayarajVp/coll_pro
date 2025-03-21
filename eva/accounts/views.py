from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session.set_expiry(0)  # Keeps session active even after closing browser
            return redirect("dashboard")
        else:
            return render(request, "login.html", {"error": "Invalid credentials"})
    return render(request, "login.html")

@login_required
def dashboard(request):
    return render(request, "dashboard.html", {"user": request.user})

def logout_view(request):
    logout(request)
    return redirect("login")
def host_event(request):
    return render(request, 'host_event.html')

def view_event(request):
    return render(request, 'view_event.html')

def raise_complaint(request):
    return render(request, 'raise_complaint.html')

def view_complaint(request):
    return render(request, 'view_complaint.html')
