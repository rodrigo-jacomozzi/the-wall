from django.contrib.auth.models import User
import uuid
from django.db import models
from django.contrib.auth.models import AbstractUser

from posts.constants import MAX_TEXT_LENGTH


class WallUser(AbstractUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)


class Post(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    text = models.CharField(max_length=MAX_TEXT_LENGTH, blank=False, null=False)
    user = models.ForeignKey(
        WallUser,
        on_delete=models.CASCADE,
        blank=False,
        null=False,
        editable=False,
        auto_created=True,
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
