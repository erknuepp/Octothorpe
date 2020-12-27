from django.conf.urls import url 
from locations import views 
 
urlpatterns = [ 
    url(r'^api/locations$', views.location_list),
    url(r'^api/locations/(?P<pk>[0-9]+)$', views.location_detail),
    url(r'^api/locations/published$', views.location_list_published)
]