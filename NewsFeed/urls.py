from django.conf.urls import url
from django.contrib import admin
from GetFeeds.views import NewsListAPIView,NewsDetailAPIView, NewsUpdateAPIView, NewsDeleteAPIView,NewsCreateAPIView

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^news/$', NewsListAPIView.as_view(), name='list'),
    url(r'^news/(?P<pk>\d+)/$', NewsDetailAPIView.as_view(), name='detail'),
    url(r'^news/(?P<pk>\d+)/edit/$', NewsUpdateAPIView.as_view(), name='update'),
    url(r'^news/(?P<pk>\d+)/delete/$', NewsDeleteAPIView.as_view(), name='delete'),
    url(r'^news/create/$', NewsCreateAPIView.as_view(), name='create'),

]
