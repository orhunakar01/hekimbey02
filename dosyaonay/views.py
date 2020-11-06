from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render

from login.views import login_view
from .forms import DosyaYukleForm2
from .models import DosyaOnay
from django.shortcuts import render , redirect , get_object_or_404 , HttpResponseRedirect , HttpResponse
from dosyayukle.forms import DosyaYukleForm
from .models import DosyaYukle


@login_required(login_url=login_view)
def dosyaonay_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = DosyaYukle.objects.all().order_by('-pk')
    # elif request.user.is_staff and request.user.username=='bursa':
    #     listele=DosyaYukle.objects.all().filter(isyeri__isyeriAdi='BURSA').order_by('-pk')
    else:
        listele = DosyaYukle.objects.filter(Olusturan=request.user).order_by('-pk')
    return render(request , 'dosyaonay/views.html' , {'listele': listele})


@login_required(login_url=login_view)
def dosyaonay_detail(request , pk):
    liste = get_object_or_404(DosyaYukle , id=pk)
    context = {'liste': liste}
    return render(request , 'dosyaonay/create.html' , context)


@login_required(login_url=login_view)
@permission_required('dosyaonay.add_dosya onay' , login_url=dosyaonay_view)
def dosyaonay_create(request):
    create6 = DosyaYukleForm2(request.POST or None , request.FILES)
    context = {'create6': create6}
    if request.method == "POST":
        if create6.is_valid():
            create6.save()
            return redirect('dosyaonay_view')
    return render(request , 'dosyaonay/create.html' , context)


@login_required(login_url=login_view)
@permission_required('dosyaonay.change_dosya onay' , login_url=dosyaonay_view)
def dosyaonay_update(request , pk):
    liste = get_object_or_404(DosyaYukle , id=pk)
    create6 = DosyaYukleForm2(request.POST or None , request.FILES or None , instance=liste)
    if create6.is_valid():
        create6.save()
        return redirect('dosyaonay_view')
    context = {'create6': create6}
    return render(request , 'dosyaonay/create.html' , context)


@login_required(login_url=login_view)
@permission_required('dosyaonay.delete_dosya onay' , login_url=dosyaonay_view)
def dosyaonay_delete(request , pk):
    liste = DosyaYukle.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('dosyaonay_view')



@login_required(login_url=login_view)
def onayli(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = DosyaYukle.objects.filter(onay=True).order_by('-pk')
    # elif request.user.is_staff and  request.user.username=='bursa':
    #     listele=DosyaYukle.objects.all().filter(isyeri__isyeriAdi='BURSA',onay=True).order_by('-pk')
    else:
        listele = DosyaYukle.objects.filter(Olusturan=request.user,onay=True).order_by('-pk')
    return render(request,'dosyaonay/onayli.html',{'listele': listele})

@login_required(login_url=login_view)
def onaysiz(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = DosyaYukle.objects.filter(red=True).order_by('-pk')
    # elif request.user.is_staff and  request.user.username=='bursa':
    #     listele=DosyaYukle.objects.all().filter(isyeri__isyeriAdi='BURSA',red=True).order_by('-pk')
    else:
        listele = DosyaYukle.objects.filter(Olusturan=request.user,red=True).order_by('-pk')
    return render(request,'dosyaonay/onaysiz.html',{'listele': listele})


@login_required(login_url=login_view)
def beklemede(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = DosyaYukle.objects.filter(red=False,onay=False).order_by('-pk')
    # elif request.user.is_staff and  request.user.username=='bursa':
    #     listele=DosyaYukle.objects.all().filter(isyeri__isyeriAdi='BURSA',red=False,onay=False).order_by('-pk')
    else:
        listele = DosyaYukle.objects.filter(Olusturan=request.user,red=False,onay=False).order_by('-pk')
    return render(request,'dosyaonay/beklemede.html',{'listele': listele})
