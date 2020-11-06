from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render , redirect , get_object_or_404
from login.views import login_view
from .forms import isyeriForm
from .models import isyeri


@login_required(login_url=login_view)
def isyeriekle_view(request):
    listele = isyeri.objects.all().order_by('pk')
    return render(request , 'isyeriekle/views.html' , {'listele': listele})


@login_required(login_url=login_view)
def isyeriekle_detail(request , pk):
    liste = get_object_or_404(isyeri , id=pk)
    context = {'liste': liste}
    return render(request , 'isyeriekle/create.html' , context)


@login_required(login_url=login_view)
@permission_required('isyeriekle.add_isyeri',login_url=isyeriekle_view)
def isyeriekle_create(request):
    create = isyeriForm(request.POST or None , request.FILES or None)
    context = {'create': create}
    if request.method == "POST":
        if create.is_valid():
            a = create.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('isyeriekle_view')
    return render(request , 'isyeriekle/create.html' , context)


@login_required(login_url=login_view)
@permission_required('isyeriekle.change_isyeri',login_url=isyeriekle_view)
def isyeri_update(request , pk):
    liste = get_object_or_404(isyeri , id=pk)
    create = isyeriForm(request.POST or None , request.FILES or None , instance=liste)
    if create.is_valid():
        create.save()
        return redirect('isyeriekle_view')
    context = {'create': create}
    return render(request , 'isyeriekle/create.html' , context)

@login_required(login_url=login_view)
@permission_required('isyeriekle.delete_isyeri',login_url=isyeriekle_view)
def isyeriekle_delete(request , pk):
    liste = isyeri.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('isyeriekle_view')
