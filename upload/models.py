from django.db import models
from django.contrib.auth.models import User

from photos.models import Like
# from django.apps import apps
# Like = apps.get_model('photos', 'Like')


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    likes = models.ManyToManyField(User, through=Like)
    publish = models.BooleanField(default=False, editable=True)

    def get_num_of_likes(self):
        return len(self.likes.all())
