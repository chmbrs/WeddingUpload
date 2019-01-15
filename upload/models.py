from django.db import models
from django.contrib.auth.models import User

from django.utils.text import slugify


class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    likes = models.ManyToManyField(User, blank=True)
    publish = models.BooleanField(default=False, editable=True)
    slug = models.SlugField(allow_unicode=True, unique=True)

    def num_of_likes(self):
        return len(self.likes.all())

    def liked_by(self):
        return ", gi".join([str(p) for p in self.likes.all()])

    def save(self, *args, **kwargs):
        self.slug = slugify(self.upload)
        super().save(*args,**kwargs)
