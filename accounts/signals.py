from django.db.models.signals import post_save, pre_save
from django.dispatch import receiver
from .models import User, UserProfile

@receiver(post_save, sender=User)
def post_save_create_profile_receiver(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)
        print("User profile is created.")
    else:
        try:
            # Updation of UserProfile
            profile = UserProfile.objects.get(user=instance)
            profile.save
            print(f"{profile.user } is saved")
        except:
        # UserProfile does not already exist for the User already created before.
            UserProfile.objects.create(user=instance)
            print("UserProfile does not already exist but user already exit, Userprofile is created.")
@receiver(pre_save,sender=User)
def pre_save_profile_receiver(sender,instance, **kwargs):
    pass