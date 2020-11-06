from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.dosyayukle_create , name='dosyayukle_create') ,
    url(r'^update/(?P<pk>\d+)$' , views.dosyayukle_update , name='dosyayukle_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.dosyayukle_delete , name='dosyayukle_delete') ,
    #url(r'^download/(?P<pk>\d+)$' , views.download , name='download') ,
    url('', views.dosyayukle_view, name='dosyayukle_view'),

    ]