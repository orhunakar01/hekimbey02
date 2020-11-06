from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.evrakadi_create , name='evrakadi_create') ,
    url(r'^update/(?P<pk>\d+)$' , views.evrakadi_update , name='evrakadi_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.evrakadi_delete , name='evrakadi_delete') ,
    url('', views.evrakadi_view, name='evrakadi_view'),
]