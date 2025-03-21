from django.contrib import admin
from .models import Event  # Import your model

# Register the model so it appears in admin
admin.site.register(Event)