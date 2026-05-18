from django.contrib import admin
# We need to import our newly created models from our models.py file.
# The dot (.) tells Python to look in the exact same folder (our polls app) for the models file.
from .models import Poll, Choice

# Imagine the Django Admin Panel is like a receptionist's desk for our database.
# By registering a model here, we are telling the receptionist:
# "Please put a tray on your desk for the Poll and Choice tables so we can view, add, and edit them."

# Registering the Poll model so it shows up on the admin panel dashboard.
admin.site.register(Poll)

# Registering the Choice model so it shows up on the admin panel dashboard.
admin.site.register(Choice)
