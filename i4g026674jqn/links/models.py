from django.contrib.auth import get_user_model
from django.db import models

from . import utils

# Create your models here.


class Link(models.Model):
    target_url = models.URLField(max_length=200)
    description = models.CharField(max_length=200)
    identifier = models.SlugField(max_length=20, blank=True, unique=True)
    author = models.Foreignkey(
        get_user_model(), on_delete=Models.CASCADE, related_name="links"
    )
    created_date = models.DateTimeField()
    active = models.BooleanField()

    def __str__(self):
        return f"{self.identifier}"

    def save(self, *args, **kwargs):
        if not self.identifier:
            # Generate a random ID
            random_id = utils.generate_random_id()

            # Make sure there is no other link with that same ID
            while Link.objects.filter(identifier=random_id).exists():
                random_id = utils.generate_random_id()

            self.identifier = random_id

            # complete the save operation
            super().save(*args, **kwargs)
