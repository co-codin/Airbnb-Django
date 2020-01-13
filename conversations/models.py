from django.db import models
from core import models as core_models

class Conversation(core_models.TimeStampedModel):
    participants = models.ManyToManyField(
        "users.User", related_name="converstation", blank=True
    )

    def __str__(self):
        usernames = []
        for user in self.participants.all():
            usernames.append(user.username)
        return ", ".join(usernames)