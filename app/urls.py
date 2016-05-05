from django.conf.urls import url, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^picture$', views.picture),
    url(r'^yoga$', views.yoga),
    url(r'^yoga/(?P<pky>[0-9]+)/$', views.post_detail, name='post_detail'),

    url(r'^game$', views.game),
    url(r'^fire$', views.fire),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

