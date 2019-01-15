from django.db import models
from django.contrib.auth.models import User

# Due to circular dependency
# Same as ->
# from upload.models import Photo
# from django.apps import apps
# Photo = apps.get_model('upload', 'Photo')

class Like(models.Model):
    user = models.ForeignKey(User, related_name='user_likes',
                            on_delete=models.CASCADE, default=None)

    # When you define a ForeignKey, you can call the model directly
    photo = models.ForeignKey('upload.Photo', on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

    class Meta:
        unique_together = ('user', 'photo')
