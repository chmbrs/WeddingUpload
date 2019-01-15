from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Photo(models.Model):
    uploaded_at = models.DateTimeField(auto_now_add=True)
    upload = models.FileField()
    likes = models.ManyToManyField(User)
    publish = models.BooleanField(default=False, editable=True)

    def get_likes(self):
        return "\n".join([l.like for l in self.likes.all()])

    def get_num_of_likes(self):
        return len(self.likes.all())


#
# from django.contrib.auth.models import User
#
#
# class Article(models.Model):
#     title = models.CharField(max_length=50)
#     likes = models.ManyToManyField(User)
#
#     def __unicode__(self):
#         return self.title
