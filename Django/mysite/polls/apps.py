from django.apps import AppConfig
from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.utils.translation import gettext_lazy as _

class PollsConfig(AppConfig):
    name = 'polls'
    verbose_name = _("Polls")

    def ready(self):
        from .models import Voter
        from django.utils.module_loading import import_string

        @receiver(post_save, sender=Voter)
        def update_party_votes(sender, instance, created, **kwargs):
            if created:
                instance.whom.votes += 1
                instance.whom.save()

        post_save.connect(update_party_votes, sender=Voter)

        @receiver(post_delete, sender=Voter)
        def remove_party_votes(sender, instance, **kwargs):
            instance.whom.votes -= 1
            instance.whom.save()