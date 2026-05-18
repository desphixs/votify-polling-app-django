from django.shortcuts import render
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
