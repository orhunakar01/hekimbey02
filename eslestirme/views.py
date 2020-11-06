from django.shortcuts import render
from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render , redirect , get_object_or_404

from login.views import login_view
from .forms import EslestirmeForm
from .models import Eslestirme

@login_required(login_url=login_view)
def eslestirme_view(request):

    listele = Eslestirme.objects.all().order_by('pk')
    return render(request , 'eslestirme/views.html' , {'listele': listele})

@login_required(login_url=login_view)
def eslestirme_detail(request , pk):
    liste = get_object_or_404(Eslestirme , id=pk)
    context = {'liste': liste}
    return render(request , 'eslestirme/create.html' , context)

@login_required(login_url=login_view)
@permission_required('eslestirme.add_eslestirme',login_url=eslestirme_view)
def eslestirme_create(request):
    create4 = EslestirmeForm(request.POST or None , request.FILES or None)
    context = {'create4': create4}
    if request.method == "POST":
        if create4.is_valid():
            a = create4.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('eslestirme_view')
    return render(request , 'eslestirme/create.html' , context)

@login_required(login_url=login_view)
@permission_required('eslestirme.change_eslestirme',login_url=eslestirme_view)
def eslestirme_update(request,pk):
    liste = get_object_or_404(Eslestirme , id=pk)
    create4 = EslestirmeForm(request.POST or None , request.FILES or None , instance=liste)
    if create4.is_valid():
        create4.save()
        return redirect('eslestirme_view')
    context = {'create4': create4}
    return render(request , 'eslestirme/create.html' , context)

@login_required(login_url=login_view)
@permission_required('eslestirme.delete_eslestirme',login_url=eslestirme_view)
def eslestirme_delete(request,pk):
    liste = Eslestirme.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('eslestirme_view')