from django.conf.urls import url
from . import views


urlpatterns = [
    url('egitimslayt_create/' , views.egitimslayt_create , name='egitimslayt_create') ,
    url(r'^egitimslayt_update/(?P<pk>\d+)$' , views.egitimslayt_update , name='egitimslayt_update') ,
    url(r'^egitimslayt_delete/(?P<pk>\d+)$' , views.egitimslayt_delete , name='egitimslayt_delete') ,
    url('egitimslayt_view/', views.egitimslayt_view, name='egitimslayt_view'),

    url('talimatlar_create/' , views.talimatlar_create , name='talimatlar_create') ,
    url(r'^talimatlar_update/(?P<pk>\d+)$' , views.talimatlar_update , name='talimatlar_update') ,
    url(r'^talimatlar_delete/(?P<pk>\d+)$' , views.talimatlar_delete , name='talimatlar_delete') ,
    url('talimatlar_view/' , views.talimatlar_view , name='talimatlar_view') ,

    url('sertifikalar_create/' , views.sertifikalar_create , name='sertifikalar_create') ,
    url(r'^sertifikalar_update/(?P<pk>\d+)$' , views.sertifikalar_update , name='sertifikalar_update') ,
    url(r'^sertifikalar_delete/(?P<pk>\d+)$' , views.sertifikalar_delete , name='sertifikalar_delete') ,
    url('sertifikalar_view/' , views.sertifikalar_view , name='sertifikalar_view') ,

    url('egitimsoru_create/', views.egitimsoru_create, name='egitimsoru_create'),
    url(r'^egitimsoru_update/(?P<pk>\d+)$', views.egitimsoru_update, name='egitimsoru_update'),
    url(r'^egitimsoru_delete/(?P<pk>\d+)$', views.egitimsoru_delete, name='egitimsoru_delete'),
    url('egitimsoru_view/', views.egitimsoru_view, name='egitimsoru_view'),

    url('isizin_create/', views.isizin_create, name='isizin_create'),
    url(r'^isizin_update/(?P<pk>\d+)$', views.isizin_update, name='isizin_update'),
    url(r'^isizin_delete/(?P<pk>\d+)$', views.isizin_delete, name='isizin_delete'),
    url('isizin_view/', views.isizin_view, name='isizin_view'),

    url('zimmet_create/', views.zimmet_create, name='zimmet_create'),
    url(r'^zimmet_update/(?P<pk>\d+)$', views.zimmet_update, name='zimmet_update'),
    url(r'^zimmet_delete/(?P<pk>\d+)$', views.zimmet_delete, name='zimmet_delete'),
    url('zimmet_view/', views.zimmet_view, name='zimmet_view'),

    url('iskaza_create/', views.iskaza_create, name='iskaza_create'),
    url(r'^iskaza_update/(?P<pk>\d+)$', views.iskaza_update, name='iskaza_update'),
    url(r'^iskaza_delete/(?P<pk>\d+)$', views.iskaza_delete, name='iskaza_delete'),
    url('iskaza_view/', views.iskaza_view, name='iskaza_view'),

    url('corona_create/' , views.corona_create , name='corona_create') ,
    url(r'^corona_update/(?P<pk>\d+)$' , views.corona_update , name='corona_update') ,
    url(r'^corona_delete/(?P<pk>\d+)$' , views.corona_delete , name='corona_delete') ,
    url('corona_view/' , views.corona_view , name='corona_view') ,

    url('calisan_create/' , views.calisan_create , name='calisan_create') ,
    url(r'^calisan_update/(?P<pk>\d+)$' , views.calisan_update , name='calisan_update') ,
    url(r'^calisan_delete/(?P<pk>\d+)$' , views.calisan_delete , name='calisan_delete') ,
    url('calisan_view/' , views.calisan_view , name='calisan_view') ,

    url('destek_create/' , views.destek_create , name='destek_create') ,
    url(r'^destek_update/(?P<pk>\d+)$' , views.destek_update , name='destek_update') ,
    url(r'^destek_delete/(?P<pk>\d+)$' , views.destek_delete , name='destek_delete') ,
    url('destek_view/' , views.destek_view , name='destek_view') ,

    url('egitim_create/' , views.egitim_create , name='egitim_create') ,
    url(r'^egitim_update/(?P<pk>\d+)$' , views.egitim_update , name='egitim_update') ,
    url(r'^egitim_delete/(?P<pk>\d+)$' , views.egitim_delete , name='egitim_delete') ,
    url('egitim_view/' , views.egitim_view , name='egitim_view') ,

    url('calisma_create/' , views.calisma_create , name='calisma_create') ,
    url(r'^calisma_update/(?P<pk>\d+)$' , views.calisma_update , name='calisma_update') ,
    url(r'^calisma_delete/(?P<pk>\d+)$' , views.calisma_delete , name='calisma_delete') ,
    url('calisma_view/' , views.calisma_view , name='calisma_view') ,

    url('degerlendirme_create/' , views.degerlendirme_create , name='degerlendirme_create') ,
    url(r'^degerlendirme_update/(?P<pk>\d+)$' , views.degerlendirme_update , name='degerlendirme_update') ,
    url(r'^degerlendirme_delete/(?P<pk>\d+)$' , views.degerlendirme_delete , name='degerlendirme_delete') ,
    url('degerlendirme_view/' , views.degerlendirme_view , name='degerlendirme_view') ,

    url('onayli_create/' , views.onayli_create , name='onayli_create') ,
    url(r'^onayli_update/(?P<pk>\d+)$' , views.onayli_update , name='onayli_update') ,
    url(r'^onayli_delete/(?P<pk>\d+)$' , views.onayli_delete , name='onayli_delete') ,
    url('onayli_view/' , views.onayli_view , name='onayli_view') ,

    url('isteslim_create/' , views.isteslim_create , name='isteslim_create') ,
    url(r'^isteslim_update/(?P<pk>\d+)$' , views.isteslim_update , name='isteslim_update') ,
    url(r'^isteslim_delete/(?P<pk>\d+)$' , views.isteslim_delete , name='isteslim_delete') ,
    url('isteslim_view/' , views.isteslim_view , name='isteslim_view') ,

    url('saha_create/' , views.saha_create , name='saha_create') ,
    url(r'^saha_update/(?P<pk>\d+)$' , views.saha_update , name='saha_update') ,
    url(r'^saha_delete/(?P<pk>\d+)$' , views.saha_delete , name='saha_delete') ,
    url('saha_view/' , views.saha_view , name='saha_view') ,

    url('kurul_create/' , views.kurul_create , name='kurul_create') ,
    url(r'^kurul_update/(?P<pk>\d+)$' , views.kurul_update , name='kurul_update') ,
    url(r'^kurul_delete/(?P<pk>\d+)$' , views.kurul_delete , name='kurul_delete') ,
    url('kurul_view/' , views.kurul_view , name='kurul_view') ,

    url('yonerge_create/' , views.yonerge_create , name='yonerge_create') ,
    url(r'^yonerge_update/(?P<pk>\d+)$' , views.yonerge_update , name='yonerge_update') ,
    url(r'^yonerge_delete/(?P<pk>\d+)$' , views.yonerge_delete , name='yonerge_delete') ,
    url('yonerge_view/' , views.yonerge_view , name='yonerge_view') ,

    url('ekip_create/' , views.ekip_create , name='ekip_create') ,
    url(r'^ekip_update/(?P<pk>\d+)$' , views.ekip_update , name='ekip_update') ,
    url(r'^ekip_delete/(?P<pk>\d+)$' , views.ekip_delete , name='ekip_delete') ,
    url('ekip_view/' , views.ekip_view , name='ekip_view') ,

    url('saglik_create/' , views.saglik_create , name='saglik_create') ,
    url(r'^saglik_update/(?P<pk>\d+)$' , views.saglik_update , name='saglik_update') ,
    url(r'^saglik_delete/(?P<pk>\d+)$' , views.saglik_delete , name='saglik_delete') ,
    url('saglik_view/' , views.saglik_view , name='saglik_view') ,

    url('acil_create/' , views.acil_create , name='acil_create') ,
    url(r'^acil_update/(?P<pk>\d+)$' , views.acil_update , name='acil_update') ,
    url(r'^acil_delete/(?P<pk>\d+)$' , views.acil_delete , name='acil_delete') ,
    url('acil_view/' , views.acil_view , name='acil_view') ,

    url('diger_create/' , views.diger_create , name='diger_create') ,
    url(r'^diger_update/(?P<pk>\d+)$' , views.diger_update , name='diger_update') ,
    url(r'^diger_delete/(?P<pk>\d+)$' , views.diger_delete , name='diger_delete') ,
    url('diger_view/' , views.diger_view , name='diger_view') ,

    url('diger2_create/' , views.diger2_create , name='diger2_create') ,
    url(r'^diger2_update/(?P<pk>\d+)$' , views.diger2_update , name='diger2_update') ,
    url(r'^diger2_delete/(?P<pk>\d+)$' , views.diger2_delete , name='diger2_delete') ,
    url('diger2_view/' , views.diger2_view , name='diger2_view') ,

    url('' , views.anasayfa_view , name='anasayfa_view') ,

    ]