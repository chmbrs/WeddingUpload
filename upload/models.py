from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify

from django import template
register = template.Library()

from photos.models import Like
# from django.apps import apps
# Like = apps.get_model('photos', 'Like')


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    likes = models.ManyToManyField(User, blank=True)
    publish = models.BooleanField(default=True, editable=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def get_num_of_likes(self):
        return len(self.likes.all())

    def save(self, *args, **kwargs):
        self.slug = slugify(self.upload)
        super().save(*args,**kwargs)
