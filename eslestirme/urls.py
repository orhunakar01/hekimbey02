from django.conf.urls import url
from . import views

urlpatterns = [
    url('create/' , views.eslestirme_create , name='eslestirme_create') ,
    url(r'^update/(?P<pk>\d+)$' , views.eslestirme_update , name='eslestirme_update') ,
    url(r'^delete/(?P<pk>\d+)$' , views.eslestirme_delete , name='eslestirme_delete') ,
    url('', views.eslestirme_view, name='eslestirme_view'),

    ]