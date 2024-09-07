from django.db.models.signals import pre_save,post_save
from .models import User,Profile
from django.dispatch import receiver
import json


@receiver(pre_save, sender=User)
def create_user(sender, instance,  **kwargs):
    
    profile = Profile.objects.create()
    
    instance.profile = profile

    
    print('client signal test not created')