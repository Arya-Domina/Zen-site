from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^picture$', views.picture),
    url(r'^music$', views.music),
    url(r'^yoga$', views.yoga),

    url(r'^yoga/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),

    url(r'^game$', views.game),
    url(r'^fire$', views.fire),
]

