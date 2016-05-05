from django.contrib import admin
from music.models import MusicPost, Musical


class PostCom(admin.StackedInline):
    model = Musical
    extra = 2


class PostAdmin(admin.ModelAdmin):
    fields = ['title', 'datetime', 'content', 'image']
    inlines = [PostCom]
    list_filter = ['datetime']

admin.site.register(MusicPost, PostAdmin)
