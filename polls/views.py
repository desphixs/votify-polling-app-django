from django.shortcuts import render, get_object_or_404
# We need Django's timezone module because we are going to stamp our polls
# with exact expiration times. Timezone ensures we avoid timezone-offset bugs.
from django.utils import timezone
# We must import the Poll database model blueprint so we can fetch records.
from .models import Poll

# Think of a View function like a chef at a restaurant.
# The user (customer) sends a Request (order), and the chef prepares the ingredients
# (fetches data from the database) and plates it in the HTML template (the final dish).
def poll_list(request):
    # Think of this query like asking a filing cabinet clerk:
    # "Please pull out ALL active folders from the Poll drawer."
    # We fetch all the Poll objects currently sitting in our SQLite database.
    # We sort them using '-id' so the newest questions are placed at the very top.
    polls = Poll.objects.all().order_by('-id')

    # Think of 'context' like a wooden serving tray.
    # We load our fetched data (polls) and the current timestamp onto the tray
    # so we can carry them safely over to our HTML presentation template.
    context = {
        'polls': polls,
        # We pass the current date and time so the template can compare it
        # with each poll's expiration date to see if it is still open for voting!
        'current_time': timezone.now(),
    }

    # Here we send the tray (context) to the template (polls/poll_list.html).
    # Django will blend them together and send a completed webpage back to the user's browser.
    return render(request, 'polls/poll_list.html', context)


# Think of a Detail View function like a museum tour guide.
# The user asks to see a very specific exhibit (a poll ID), and the guide
# fetches that exact item and shows all its details.
def poll_detail(request, poll_id):
    # Think of get_object_or_404 like a security guard.
    # We ask the guard to find the Poll with the exact ID requested.
    # If the poll does not exist, the guard stops the visitor and politely shows them
    # a "404 Not Found" exit page instead of letting the application crash.
    poll = get_object_or_404(Poll, pk=poll_id)

    # Think of this query like asking our relational balloons (Choices):
    # "Hey, please find all the balloons tethered to this specific post (Poll)."
    # We fetch all the Choice objects connected to this Poll database record.
    choices = poll.choices.all()

    # Think of this check like an automated gate at a subway station.
    # We compare the current time with the poll's expiration time.
    # If the current clock time is PAST the deadline, the gate locks (is_expired = True).
    is_expired = timezone.now() > poll.expiration_date

    # Think of 'context' like our wooden serving tray again.
    # We load our single poll, all its choices, and the expiration status onto the tray.
    context = {
        'poll': poll,
        'choices': choices,
        'is_expired': is_expired,
    }

    # Here we hand our tray (context) to the template (polls/poll_detail.html).
    # Django will blend them together and send a completed detail webpage back to the user.
    return render(request, 'polls/poll_detail.html', context)
