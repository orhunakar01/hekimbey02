from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render , redirect , get_object_or_404

from login.views import login_view
from .forms import EvrakAdiForm
from .models import EvrakAdi

@login_required(login_url=login_view)
def evrakadi_view(request):
    listele = EvrakAdi.objects.all().order_by('sira_no')
    return render(request , 'evrakAdi/views.html' , {'listele': listele})

@login_required(login_url=login_view)
def evrakadi_detail(request , pk):
    liste = get_object_or_404(EvrakAdi , id=pk)
    context = {'liste': liste}
    return render(request , 'evrakAdi/create.html' , context)

@login_required(login_url=login_view)
@permission_required('evrakAdi.add_evrak adi',login_url=evrakadi_view)
def evrakadi_create(request):
    create3 = EvrakAdiForm(request.POST or None , request.FILES or None)
    context = {'create3': create3}
    if request.method == "POST":
        if create3.is_valid():
            a = create3.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('evrakadi_view')
    return render(request , 'evrakAdi/create.html' , context)

@login_required(login_url=login_view)
@permission_required('evrakAdi.change_evrak adi',login_url=evrakadi_view)
def evrakadi_update(request, pk):
    liste = get_object_or_404(EvrakAdi , id=pk)
    create3 = EvrakAdiForm(request.POST or None , instance=liste)
    if create3.is_valid():
        create3.save()
        return redirect('evrakadi_view')
    context = {'create3': create3}
    return render(request , 'evrakAdi/create.html' , context)

@login_required(login_url=login_view)
@permission_required('evrakAdi.delete_evrak adi',login_url=evrakadi_view)
def evrakadi_delete(request,pk):
    liste = EvrakAdi.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('evrakadi_view')