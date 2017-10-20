from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home_page, name='home_page'),
    url(r'^(?P<pk>\d+)/$', views.post_detail, name='post_detail'),
]
