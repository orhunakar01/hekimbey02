from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render , redirect , get_object_or_404

from login.views import login_view
from .forms import calisilanFirmalarForm
from .models import calisilanFirmalar

@login_required(login_url=login_view)
def calisilanfirma_view(request):
    listele = calisilanFirmalar.objects.all().order_by('pk')
    return render(request , 'calisilanFirma/views.html' , {'listele': listele})

@login_required(login_url=login_view)
def calisilanfirma_detail(request , pk):
    liste = get_object_or_404(calisilanFirmalar , id=pk)
    context = {'liste': liste}
    return render(request , 'calisilanFirma/create.html' , context)

@login_required(login_url=login_view)
@permission_required('calisilanFirma.add_calisilan firmalar',login_url=calisilanfirma_view)
def calisilanfirma_create(request):
    create2 = calisilanFirmalarForm(request.POST or None , request.FILES or None)
    context = {'create2': create2}
    if request.method == "POST":
        if create2.is_valid():
            a = create2.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('calisilanfirma_view')
    return render(request , 'calisilanFirma/create.html' , context)

@login_required(login_url=login_view)
@permission_required('calisilanFirma.change_calisilan firmalar',login_url=calisilanfirma_view)
def calisilanfirma_update(request , pk):
    liste = get_object_or_404(calisilanFirmalar , id=pk)
    create2 = calisilanFirmalarForm(request.POST or None , request.FILES or None , instance=liste)
    if create2.is_valid():
        create2.save()
        return redirect('calisilanfirma_view')
    context = {'create2': create2}
    return render(request , 'calisilanFirma/create.html' , context)

@login_required(login_url=login_view)
@permission_required('calisilanFirma.delete_calisilan firmalar',login_url=calisilanfirma_view)
def calisilanfirma_delete(request , pk):
    liste = calisilanFirmalar.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('calisilanfirma_view')
