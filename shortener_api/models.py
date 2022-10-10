from django.conf import settings
from django.contrib.auth.models import User
from django.db import models
from random import choices
from string import ascii_letters


class Link(models.Model):
    original_link = models.URLField()
    short_link = models.URLField(blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    counter = models.IntegerField(blank=True, null=True)

    def shortener(self):
        while True:
            random_string = ''.join(choices(ascii_letters, k=7))
            new_link = settings.HOST_URL + '/' + random_string

            if not Link.objects.filter(short_link=new_link).exists():
                break

        return new_link

    def save(self, *args, **kwargs):
        if not self.short_link:
            new_link = self.shortener()
            self.short_link = new_link
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.original_link
