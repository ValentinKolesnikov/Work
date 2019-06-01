from django.contrib import admin
from .models import Event, Like, Participant

# Register your models here.

admin.site.register(Event)
admin.site.register(Like)
admin.site.register(Participant)

