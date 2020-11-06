from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.calisilanfirma_create , name='calisilanfirma_create') ,
    url(r'^update/(?P<pk>\d+)$' , views.calisilanfirma_update , name='calisilanfirma_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.calisilanfirma_delete , name='calisilanfirma_delete') ,
    url('', views.calisilanfirma_view, name='calisilanfirma_view'),

    ]