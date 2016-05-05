import os
from django.db import models


class MusicPost(models.Model):  # альбом
    title = models.CharField(max_length=50)  # header
    content = models.TextField(max_length=255)  # text
    datetime = models.DateTimeField('Дата публикации')  # дата публикации
    image = models.ImageField(blank=True, verbose_name='Image', upload_to="media/music", null=True,)

    def __str__(self):
        return self.title

    def get_short_content(self):
        if len(self.content) > 50:
            return self.content[:50]
        else:
            return self.content


def get_absolute_url(self):
        return "/music/%i/" % self.id


class Musical(models.Model):  # песня
    title = models.ForeignKey(MusicPost)
    musicfile = models.TextField(blank=True, verbose_name='FileName. Add the full name of mp3 file. Exchange space into "_"')
    name = models.TextField(blank=True, verbose_name='Song Name')
    artist = models.TextField(blank=True, verbose_name='Artist Name')
    music = models.FileField(blank=True, verbose_name='Music', upload_to="media/music", null=True)

    def filename(self):
        return os.path.basename(self.file.name)


