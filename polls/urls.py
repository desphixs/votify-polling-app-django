from django.urls import path
# We import the views module from our current folder (our polls app)
from . import views

# Imagine URL paths like signposts in an amusement park.
# They direct visitors to the correct ride (our view functions) when they type a address.
urlpatterns = [
    # Think of this empty path as the main entrance gate of our park (the homepage).
    # When a visitor goes to the main website URL, they are directed to the 'poll_list' view.
    path('', views.poll_list, name='poll_list'),
]
