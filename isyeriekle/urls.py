from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.isyeriekle_create , name='isyeriekle_create') ,
    url(r'^update/(?P<pk>\d+)$' , views.isyeri_update , name='isyeri_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.isyeriekle_delete , name='isyeriekle_delete') ,
    url('', views.isyeriekle_view, name='isyeriekle_view'),
]

