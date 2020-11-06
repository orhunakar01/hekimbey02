from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.dosyaonay_create , name='dosyaonay_create') ,
    url('onayli/' , views.onayli , name='onayli') ,
    url('onaysiz/' , views.onaysiz , name='onaysiz') ,
    url('beklemede/' , views.beklemede , name='beklemede') ,
    url(r'^update/(?P<pk>\d+)$' , views.dosyaonay_update , name='dosyaonay_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.dosyaonay_delete , name='dosyaonay_delete') ,
    #url(r'^download/(?P<pk>\d+)$' , views.download , name='download') ,
    url('', views.dosyaonay_view, name='dosyaonay_view'),

    ]