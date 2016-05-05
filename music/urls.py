from django.conf.urls import patterns, url
from music import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = patterns(
    '',
    url(r'^musicpost', views.articles),
    url(r'^musicality/(?P<pkm>[0-9]+)/$', views.post_detail,  name='post_detail'),
    ) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
