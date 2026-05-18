from django.db import models

# Imagine a database like a giant filing cabinet, and Django models are blueprints
# or instruction manuals on how to construct the folders (tables) inside this cabinet.
# Here, we are creating a blueprint for our Poll table in the database.
class Poll(models.Model):
    # Think of a CharField like a single-line label maker. 
    # We use it to store short text. In this case, it stores our actual polling question.
    # We limit it to 200 characters to keep our questions punchy and clean.
    question = models.CharField(max_length=200)

    # Think of a DateTimeField like a digital clock stamped on a milk carton.
    # It tells us the exact year, month, day, hour, and minute when this poll
    # goes bad (expires) and will no longer accept any votes from our community.
    expiration_date = models.DateTimeField()

    # The __str__ method is like a nametag on a person at a party.
    # When Django wants to show this poll in the admin dashboard or the command line,
    # instead of displaying an anonymous "Poll object (1)", it proudly returns
    # the actual question text so we humans know exactly which poll we are looking at.
    def __str__(self):
        return self.question


# Now we need a blueprint for the Choice table.
# Each Choice is like a ballot option on a physical voting card.
class Choice(models.Model):
    # Think of a ForeignKey like a strong tether or a string connecting a balloon to a post.
    # Here, we tether each Choice to a specific Poll.
    # 'on_delete=models.CASCADE' means if we delete a Poll question,
    # we want all of its choices to be automatically thrown in the trash as well,
    # so we don't have orphan choices floating around with no question.
    # 'related_name="choices"' lets us easily ask a Poll: "hey, what choices do you have?"
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE, related_name='choices')

    # This CharField is the actual text of our choice (e.g., "Python" or "JavaScript").
    # It acts like a label for the option on our voting card.
    option_text = models.CharField(max_length=200)

    # Think of an IntegerField like a scoreboard counter at a sports match.
    # It only counts whole numbers (like 0, 1, 2, 3...).
    # We set 'default=0' because when we first create a choice,
    # absolutely nobody has voted for it yet, so it must start at zero!
    votes = models.IntegerField(default=0)

    # Again, this __str__ method acts as the nametag for this choice,
    # so in the Django admin panel, we see the option text (e.g., "Python")
    # instead of just "Choice object (1)".
    def __str__(self):
        return self.option_text
