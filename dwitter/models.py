from django.contrib.auth.models import User
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


class Dweet(models.Model):
    user = models.ForeignKey(
        User, related_name="dweets",  on_delete=models.DO_NOTHING
    )
    body = models.CharField(max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{self.body[:30]}..."
        )


class Favourite_pages(models.Model):
    logo =  models.ImageField(upload_to='favourite/%Y/%m/%d/',blank=True)
    description = models.CharField(max_length=200,default='page intro')
    url_link = models.CharField(max_length=2000,default='page link')


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    follows = models.ManyToManyField(
        "self", related_name="followed_by", symmetrical=False, blank=True
    )
    date_of_birth = models.DateField(blank=True, null=True)
    photo = models.ImageField(upload_to='users/%Y/%m/%d/',blank=True)
    dashboard_pic = models.ImageField(upload_to='dashboard/%Y/%m/%d/',blank=True)
    profile_intro = models.CharField(max_length=1000,default='my profile intro',null=True,blank= True)
    fav_page = models.ForeignKey(Favourite_pages, related_name='favouritePage', on_delete=models.CASCADE,null=True)

    def __str__(self):
        return self.user.username

    @property
    def get_photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url
        else:
            return "/static/images/user.jpg"


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user=instance)
        user_profile.save()
        user_profile.follows.add(instance.profile)
        user_profile.save()
