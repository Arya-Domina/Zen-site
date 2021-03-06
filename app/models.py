from django.db import models


class YogaPost(models.Model):
    title = models.CharField(max_length=255)
    text = models.TextField()
    image = models.ImageField(blank=True, upload_to="yoga")

    def publish(self):
        self.save()

    def __str__(self):
        return self.title
