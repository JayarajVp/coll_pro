from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import Event, Complaint
from django.http import JsonResponse

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

def submit_event(request):
    if request.method == "POST":
        host_name = request.POST.get("host_name")
        event_name = request.POST.get("event_name")
        event_description = request.POST.get("event_description")

        Event.objects.create(host_name=host_name, event_name=event_name, event_description=event_description)

        return redirect("dashboard")  # Redirect back to dashboard after submission

    return render(request, "host_event.html")

def submit_complaint(request):
    if request.method == "POST":
        roll_number = request.POST.get("roll_number")
        complaint_description = request.POST.get("complaint_description")

        Complaint.objects.create(roll_number=roll_number, complaint_description=complaint_description)

        return redirect("dashboard")  # Redirect back after submission

    return render(request, "register_complaint.html")
def view_event(request):
    events = Event.objects.all()
    
    # Debugging: Print each event's details in the console
    for event in events:
        print(f"Event: {event.event_name}, Description: {event.event_description}")  # Fix here
    
    return render(request, "view_event.html", {"events": events})

def view_complaint(request):
    if request.method == "GET" and "roll_no" in request.GET:
        roll_no = request.GET.get("roll_no")

        if not roll_no:  # If roll number is empty, return error
            return JsonResponse({"error": "Roll number is required!"}, status=400)

        complaints = Complaint.objects.filter(roll_number=roll_no).values("roll_number", "complaint_description", "date_submitted")
        return JsonResponse({"complaints": list(complaints)})

    # If no roll_no is provided, return the HTML file
    return render(request, "view_complaint.html")


    