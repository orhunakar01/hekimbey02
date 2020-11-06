from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render , redirect , get_object_or_404,HttpResponseRedirect , HttpResponse

from isyeriekle.models import isyeri
from login.views import login_view
from .forms import DosyaYukleForm
from .models import DosyaYukle



@login_required(login_url=login_view)
def dosyayukle_view(request):
    if request.user.is_staff or request.user.is_superuser:
        listele = DosyaYukle.objects.all().order_by('-pk')
    # elif request.user.is_staff and  request.user.username=='bursa':
    #     listele=DosyaYukle.objects.all().filter(isyeri__isyeriAdi='BURSA').order_by('-pk')
    else:
        listele=DosyaYukle.objects.filter(Olusturan=request.user).order_by('-pk')
    return render(request , 'dosyayukle/views.html' , {'listele': listele})

@login_required(login_url=login_view)
def dosyayukle_detail(request,pk):
    liste = get_object_or_404(DosyaYukle , id=pk)
    context = {'liste': liste}
    return render(request , 'dosyayukle/create.html' , context)


@login_required(login_url=login_view)
# @permission_required('dosyayukle.add_dosya yukle',login_url=dosyayukle_view)
def dosyayukle_create(request):
    create5 = DosyaYukleForm(request.POST or None , request.FILES)
    context = {'create5': create5}
    if request.method == "POST":
        if create5.is_valid():
            create5.save()
            return redirect('dosyayukle_view')
    return render(request , 'dosyayukle/create.html' , context)

@login_required(login_url=login_view)
# @permission_required('dosyayukle.change_dosya yukle',login_url=dosyayukle_view)
def dosyayukle_update(request,pk):
    liste = get_object_or_404(DosyaYukle , id=pk)
    create5 = DosyaYukleForm(request.POST or None , request.FILES or None , instance=liste)
    if create5.is_valid():
        create5.save()
        return redirect('dosyayukle_view')
    context = {'create5': create5}
    return render(request , 'dosyayukle/create.html' , context)

@login_required(login_url=login_view)
# @permission_required('dosyayukle.delete_dosya yukle',login_url=dosyayukle_view)
def dosyayukle_delete(request,pk):
    liste = DosyaYukle.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('dosyayukle_view')


"""def download(request , pk):
    listele = get_object_or_404(DosyaYukle , id=pk)
    file_path = listele.dosya.path
    file_name = str(listele.dosya)

    fh = open(file_path , 'rb')
    mime_type , _ = mimetypes.guess_type(file_path)
    response = HttpResponse(fh , content_type=mime_type)
    response['Content-Disposition'] = f"attachment; filename={file_name}"
    return response"""


