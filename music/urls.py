from django.conf.urls import url
from . import views


app_name = 'music'


urlpatterns = [
    # /music/
    url(r'^$', views.IndexView.as_view(), name='index'),

    # music/71(id)
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='details'),

    # music/album/add
    url(r'album/add/$', views.AlbumCreate.as_view(), name='album_add'),

    # music/album/2
    url(r'album/(?P<pk>[0-9]+)/$', views.AlbumUpdate.as_view(), name='album_update'),

    # music/album/2/delete
    url(r'album/(?P<pk>[0-9]+)/delete/$', views.AlbumDelete.as_view(), name='album_delete'),
]
