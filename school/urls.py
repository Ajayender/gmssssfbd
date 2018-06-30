from django.conf.urls import url
from school import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    url(r'^$',views.AboutView,name='about'),
    url(r'^news/$',views.LatestnewsListView.as_view(),name='news_list'),
    url(r'^news/(?P<pk>\d+)/$',views.LatestnewsDetailView.as_view(),name='news_details'),
    url(r'^gallery/$',views.AlbumListView.as_view(),name='album_list'),
    url(r'^hof/$',views.HOF.as_view(),name='hof'),
    url(r'^staff/$',views.Staff.as_view(),name='staff'),
    url(r'^gallery/(?P<pk>\d+)/$',views.AlbumDetailView.as_view(),name='album_details'),
    url(r'^reach_us/$',views.ReachUs.as_view(),name='reachus'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
