from django.db import models

class URL(models.Model):
    url_original = models.CharField(max_length=255)
    url_short = models.CharField(max_length=100)

    def __str__(self):
        return self.url_original
