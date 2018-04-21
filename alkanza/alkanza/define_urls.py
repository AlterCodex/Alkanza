from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$',views.home,name='home'),
	url(r'^search_place/(?P<place_id>[0-9A-Za-z_\-]+)/(?P<key>[0-9A-Za-z_\-]+)/$',views.search_place,name="search_place"),
]
