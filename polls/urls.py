from django.urls import path
# We import the views module from our current folder (our polls app)
from . import views

# Imagine URL paths like signposts in an amusement park.
# They direct visitors to the correct ride (our view functions) when they type an address.
urlpatterns = [
    # Think of this empty path as the main entrance gate of our park (the homepage).
    # When a visitor goes to the main website URL, they are directed to the 'poll_list' view.
    path('', views.poll_list, name='poll_list'),

    # Think of this path like a signpost pointing to a specific room inside our gaming lounge.
    # The '<int:poll_id>' is a dynamic variable slot. If a user visits '/poll/4/',
    # Django grabs the number 4 and hands it to the 'poll_detail' view function.
    path('poll/<int:poll_id>/', views.poll_detail, name='poll_detail'),

    # Think of this path like a secure ballot dropbox slot. When a voter drops their dynamic
    # choice sheet into '/poll/4/vote/', Django forwards their card directly to the 'vote' official.
    path('poll/<int:poll_id>/vote/', views.vote, name='vote'),
]
