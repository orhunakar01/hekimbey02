from django.contrib.auth.decorators import login_required , permission_required
from django.shortcuts import render, redirect, get_object_or_404
from login.views import login_view
from .forms import EgitimSlaytlariForm , talimatlarForm , sertifikalarForm , egitimSoruForm , isizinForm , zimmetForm , \
    iskazaForm , coronaForm , calisanForm , destekForm , egitimForm , calismaForm , degerlendirmeForm , onayliForm , \
    isteslimForm , sahaForm , kurulForm , yonergeForm , ekipForm , saglikForm , acilForm , digerForm , digerForm2
from .models import egitimSlaytlari , talimatlar , sertifikalar , egitimSoru , isizin , zimmet , iskaza , corona , \
    calisan , destek , egitim , calisma , degerlendirme , onayli , isteslim , saha , kurul , yonerge , ekip , saglik , \
    acil , diger , diger2


@login_required(login_url=login_view)
def anasayfa_view(request):
    return render(request, 'dokumanlar/anasayfa.html')


@login_required(login_url=login_view)
def egitimslayt_view(request):
    listele = egitimSlaytlari.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views.html', {'listele': listele})

@permission_required('dokumanlar.add_egitim slaytlari',login_url=egitimslayt_view)
@login_required(login_url=login_view)
def egitimslayt_create(request):
    create7 = EgitimSlaytlariForm(request.POST or None, request.FILES or None)
    context = {'create7': create7}
    if request.method == "POST":
        if create7.is_valid():
            a = create7.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('egitimslayt_view')
    return render(request, 'dokumanlar/create.html', context)

@permission_required('dokumanlar.change_egitim slaytlari',login_url=egitimslayt_view)
@login_required(login_url=login_view)
def egitimslayt_update(request, pk):
    liste = get_object_or_404(egitimSlaytlari, id=pk)
    create7 = EgitimSlaytlariForm(request.POST or None, request.FILES or None, instance=liste)
    if create7.is_valid():
        create7.save()
        return redirect('egitimslayt_view')
    context = {'create7': create7}
    return render(request, 'dokumanlar/create.html', context)


@permission_required('dokumanlar.delete_egitim slaytlari',login_url=egitimslayt_view)
@login_required(login_url=login_view)
def egitimslayt_delete(request, pk):
    liste = egitimSlaytlari.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('egitimslayt_view')


# -------------------------------2-------------------------------------- #
@login_required(login_url=login_view)
def talimatlar_view(request):
    listele = talimatlar.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views2.html', {'listele': listele})

@permission_required('dokumanlar.add_talimatlar',login_url=talimatlar_view)
@login_required(login_url=login_view)
def talimatlar_create(request):
    create8 = talimatlarForm(request.POST or None, request.FILES or None)
    context = {'create8': create8}
    if request.method == "POST":
        if create8.is_valid():
            a = create8.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('talimatlar_view')
    return render(request, 'dokumanlar/create2.html', context)


@permission_required('dokumanlar.change_talimatlar',login_url=talimatlar_view)
@login_required(login_url=login_view)
def talimatlar_update(request, pk):
    liste = get_object_or_404(talimatlar, id=pk)
    create8 = talimatlarForm(request.POST or None, request.FILES or None, instance=liste)
    if create8.is_valid():
        create8.save()
        return redirect('talimatlar_view')
    context = {'create8': create8}
    return render(request, 'dokumanlar/create2.html', context)


@permission_required('dokumanlar.delete_talimatlar',login_url=talimatlar_view)
@login_required(login_url=login_view)
def talimatlar_delete(request, pk):
    liste = talimatlar.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('egitimslayt_view')


#  ----------------3-------------------  #


@login_required(login_url=login_view)
def sertifikalar_view(request):
    listele = sertifikalar.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views3.html', {'listele': listele})

@permission_required('dokumanlar.add_sertifikalar',login_url=sertifikalar_view)
@login_required(login_url=login_view)
def sertifikalar_create(request):
    create9 = sertifikalarForm(request.POST or None, request.FILES or None)
    context = {'create9': create9}
    if request.method == "POST":
        if create9.is_valid():
            a = create9.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('sertifikalar_view')
    return render(request, 'dokumanlar/create3.html', context)


@permission_required('dokumanlar.change_sertifikalar',login_url=sertifikalar_view)
@login_required(login_url=login_view)
def sertifikalar_update(request, pk):
    liste = get_object_or_404(sertifikalar, id=pk)
    create9 = sertifikalarForm(request.POST or None, request.FILES or None, instance=liste)
    if create9.is_valid():
        create9.save()
        return redirect('sertifikalar_view')
    context = {'create9': create9}
    return render(request, 'dokumanlar/create3.html', context)


@permission_required('dokumanlar.delete_sertifikalar',login_url=sertifikalar_view)
@login_required(login_url=login_view)
def sertifikalar_delete(request, pk):
    liste = sertifikalar.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('sertifikalar_view')


# -------------------4----------------------- #
@login_required(login_url=login_view)
def egitimsoru_view(request):
    listele = egitimSoru.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views4.html', {'listele': listele})


@permission_required('dokumanlar.add_egitim soru',login_url=egitimsoru_view)
@login_required(login_url=login_view)
def egitimsoru_create(request):
    create10 = egitimSoruForm(request.POST or None, request.FILES or None)
    context = {'create10': create10}
    if request.method == "POST":
        if create10.is_valid():
            a = create10.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('egitimsoru_view')
    return render(request, 'dokumanlar/create4.html', context)


@permission_required('dokumanlar.change_egitim soru',login_url=egitimsoru_view)
@login_required(login_url=login_view)
def egitimsoru_update(request, pk):
    liste = get_object_or_404(egitimSoru, id=pk)
    create10 = egitimSoruForm(request.POST or None, request.FILES or None, instance=liste)
    if create10.is_valid():
        create10.save()
        return redirect('egitimsoru_view')
    context = {'create10': create10}
    return render(request, 'dokumanlar/create4.html', context)

@permission_required('dokumanlar.delete_egitim soru',login_url=egitimsoru_view)
@login_required(login_url=login_view)
def egitimsoru_delete(request, pk):
    liste = egitimSoru.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('egitimsoru_view')

# ------------------- 5 --------------- #

@login_required(login_url=login_view)
def isizin_view(request):
    listele = isizin.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views5.html', {'listele': listele})

@permission_required('dokumanlar.add_isizin',login_url=isizin_view)
@login_required(login_url=login_view)
def isizin_create(request):
    create11 = isizinForm(request.POST or None, request.FILES or None)
    context = {'create11': create11}
    if request.method == "POST":
        if create11.is_valid():
            a = create11.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('isizin_view')
    return render(request, 'dokumanlar/create5.html', context)


@permission_required('dokumanlar.change_isizin',login_url=isizin_view)
@login_required(login_url=login_view)
def isizin_update(request,pk):
    liste = get_object_or_404(isizin, id=pk)
    create11 = isizinForm(request.POST or None, request.FILES or None, instance=liste)
    if create11.is_valid():
        create11.save()
        return redirect('isizin_view')
    context = {'create11': create11}
    return render(request, 'dokumanlar/create5.html', context)


@permission_required('dokumanlar.delete_isizin',login_url=isizin_view)
@login_required(login_url=login_view)
def isizin_delete(request,pk):
    liste = isizin.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('isizin_view')

# --------------- 6 ----------------#


@login_required(login_url=login_view)
def zimmet_view(request):
    listele = zimmet.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views6.html', {'listele': listele})

@permission_required('dokumanlar.add_zimmet',login_url=zimmet_view)
@login_required(login_url=login_view)
def zimmet_create(request):
    create12 = zimmetForm(request.POST or None, request.FILES or None)
    context = {'create12': create12}
    if request.method == "POST":
        if create12.is_valid():
            a = create12.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('zimmet_view')
    return render(request, 'dokumanlar/create6.html', context)


@permission_required('dokumanlar.change_zimmet',login_url=zimmet_view)
@login_required(login_url=login_view)
def zimmet_update(request,pk):
    liste = get_object_or_404(zimmet, id=pk)
    create12 = zimmetForm(request.POST or None, request.FILES or None, instance=liste)
    if create12.is_valid():
        create12.save()
        return redirect('zimmet_view')
    context = {'create12': create12}
    return render(request, 'dokumanlar/create6.html', context)


@permission_required('dokumanlar.delete_zimmet',login_url=zimmet_view)
@login_required(login_url=login_view)
def zimmet_delete(request,pk):
    liste = zimmet.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('zimmet_view')

#  ----------------  7  ------------ #
@login_required(login_url=login_view)
def iskaza_view(request):
    listele = iskaza.objects.all().order_by('pk')
    return render(request, 'dokumanlar/views7.html', {'listele': listele})

@permission_required('dokumanlar.add_iskaza',login_url=iskaza_view)
@login_required(login_url=login_view)
def iskaza_create(request):
    create13 = iskazaForm(request.POST or None, request.FILES or None)
    context = {'create13': create13}
    if request.method == "POST":
        if create13.is_valid():
            a = create13.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('iskaza_view')
    return render(request, 'dokumanlar/create7.html', context)


@permission_required('dokumanlar.change_iskaza',login_url=iskaza_view)
@login_required(login_url=login_view)
def iskaza_update(request,pk):
    liste = get_object_or_404(iskaza, id=pk)
    create13 = iskazaForm(request.POST or None, request.FILES or None, instance=liste)
    if create13.is_valid():
        create13.save()
        return redirect('iskaza_view')
    context = {'create13': create13}
    return render(request, 'dokumanlar/create7.html', context)


@permission_required('dokumanlar.delete_iskaza',login_url=iskaza_view)
@login_required(login_url=login_view)
def iskaza_delete(request,pk):
    liste = iskaza.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('iskaza_view')

# ----------- 8 --------------------------#
@login_required(login_url=login_view)
def corona_view(request):
    listele = corona.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views8.html', {'listele': listele})

@permission_required('dokumanlar.add_corona',login_url=corona_view)
@login_required(login_url=login_view)
def corona_create(request):
    create14 = coronaForm(request.POST or None, request.FILES or None)
    context = {'create14': create14}
    if request.method == "POST":
        if create14.is_valid():
            a = create14.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('corona_view')
    return render(request, 'dokumanlar/create8.html', context)

@permission_required('dokumanlar.change_corona',login_url=corona_view)
@login_required(login_url=login_view)
def corona_update(request,pk):
    liste = get_object_or_404(corona, id=pk)
    create14 = coronaForm(request.POST or None, request.FILES or None, instance=liste)
    if create14.is_valid():
        create14.save()
        return redirect('corona_view')
    context = {'create14': create14}
    return render(request, 'dokumanlar/create8.html', context)

@permission_required('dokumanlar.delete_corona',login_url=corona_view)
@login_required(login_url=login_view)
def corona_delete(request,pk):
    liste = corona.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('corona_view')

# --------- 9 ---------#

@login_required(login_url=login_view)
def calisan_view(request):
    listele = calisan.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views9.html', {'listele': listele})


@permission_required('dokumanlar.add_calisan',login_url=calisan_view)
@login_required(login_url=login_view)
def calisan_create(request):
    create15 = calisanForm(request.POST or None, request.FILES or None)
    context = {'create15': create15}
    if request.method == "POST":
        if create15.is_valid():
            a = create15.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('calisan_view')
    return render(request, 'dokumanlar/create9.html', context)


@permission_required('dokumanlar.change_calisan',login_url=calisan_view)
@login_required(login_url=login_view)
def calisan_update(request,pk):
    liste = get_object_or_404(calisan, id=pk)
    create15 = calisanForm(request.POST or None, request.FILES or None, instance=liste)
    if create15.is_valid():
        create15.save()
        return redirect('calisan_view')
    context = {'create15': create15}
    return render(request, 'dokumanlar/create9.html', context)


@permission_required('dokumanlar.delete_calisan',login_url=calisan_view)
@login_required(login_url=login_view)
def calisan_delete(request,pk):
    liste = calisan.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('calisan_view')

# ------ 10  -------- #

@login_required(login_url=login_view)
def destek_view(request):
    listele = destek.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views10.html', {'listele': listele})


@permission_required('dokumanlar.add_destek',login_url=destek_view)
@login_required(login_url=login_view)
def destek_create(request):
    create16 = destekForm(request.POST or None, request.FILES or None)
    context = {'create16': create16}
    if request.method == "POST":
        if create16.is_valid():
            a = create16.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('destek_view')
    return render(request, 'dokumanlar/create10.html', context)


@permission_required('dokumanlar.change_destek',login_url=destek_view)
@login_required(login_url=login_view)
def destek_update(request,pk):
    liste = get_object_or_404(destek, id=pk)
    create16 = destekForm(request.POST or None, request.FILES or None, instance=liste)
    if create16.is_valid():
        create16.save()
        return redirect('destek_view')
    context = {'create16': create16}
    return render(request, 'dokumanlar/create10.html', context)


@permission_required('dokumanlar.delete_destek',login_url=destek_view)
@login_required(login_url=login_view)
def destek_delete(request,pk):
    liste = destek.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('destek_view')

# ----- 11 ----- #
@login_required(login_url=login_view)
def egitim_view(request):
    listele = egitim.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views11.html', {'listele': listele})

@permission_required('dokumanlar.add_egitim',login_url=egitim_view)
@login_required(login_url=login_view)
def egitim_create(request):
    create17 = egitimForm(request.POST or None, request.FILES or None)
    context = {'create17': create17}
    if request.method == "POST":
        if create17.is_valid():
            a = create17.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('egitim_view')
    return render(request, 'dokumanlar/create11.html', context)

@permission_required('dokumanlar.change_egitim',login_url=egitim_view)
@login_required(login_url=login_view)
def egitim_update(request,pk):
    liste = get_object_or_404(egitim, id=pk)
    create17 = egitimForm(request.POST or None, request.FILES or None, instance=liste)
    if create17.is_valid():
        create17.save()
        return redirect('egitim_view')
    context = {'create17': create17}
    return render(request, 'dokumanlar/create11.html', context)


@permission_required('dokumanlar.delete_egitim',login_url=egitim_view)
@login_required(login_url=login_view)
def egitim_delete(request,pk):
    liste = egitim.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('egitim_view')

# ---- 12- - -- - -- #
@login_required(login_url=login_view)
def calisma_view(request):
    listele = calisma.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views12.html', {'listele': listele})

@permission_required('dokumanlar.add_calisma',login_url=calisma_view)
@login_required(login_url=login_view)
def calisma_create(request):
    create18 = calismaForm(request.POST or None, request.FILES or None)
    context = {'create18': create18}
    if request.method == "POST":
        if create18.is_valid():
            a = create18.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('calisma_view')
    return render(request, 'dokumanlar/create12.html', context)


@permission_required('dokumanlar.change_calisma',login_url=calisma_view)
@login_required(login_url=login_view)
def calisma_update(request,pk):
    liste = get_object_or_404(calisma, id=pk)
    create18 = calismaForm(request.POST or None, request.FILES or None, instance=liste)
    if create18.is_valid():
        create18.save()
        return redirect('calisma_view')
    context = {'create18': create18}
    return render(request, 'dokumanlar/create12.html', context)


@permission_required('dokumanlar.delete_calisma',login_url=calisma_view)
@login_required(login_url=login_view)
def calisma_delete(request,pk):
    liste = calisma.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('egitim_view')

@login_required(login_url=login_view)
def degerlendirme_view(request):
    listele = degerlendirme.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views13.html', {'listele': listele})


@permission_required('dokumanlar.add_degerlendirme',login_url=degerlendirme_view)
@login_required(login_url=login_view)
def degerlendirme_create(request):
    create19 = degerlendirmeForm(request.POST or None, request.FILES or None)
    context = {'create19': create19}
    if request.method == "POST":
        if create19.is_valid():
            a = create19.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('degerlendirme_view')
    return render(request, 'dokumanlar/create13.html', context)

@permission_required('dokumanlar.change_degerlendirme',login_url=degerlendirme_view)
@login_required(login_url=login_view)
def degerlendirme_update(request,pk):
    liste = get_object_or_404(degerlendirme, id=pk)
    create19 = degerlendirmeForm(request.POST or None, request.FILES or None, instance=liste)
    if create19.is_valid():
        create19.save()
        return redirect('degerlendirme_view')
    context = {'create19': create19}
    return render(request, 'dokumanlar/create13.html', context)


@permission_required('dokumanlar.delete_degerlendirme',login_url=degerlendirme_view)
@login_required(login_url=login_view)
def degerlendirme_delete(request,pk):
    liste = degerlendirme.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('degerlendirme_view')

@login_required(login_url=login_view)
def onayli_view(request):
    listele = onayli.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views14.html', {'listele': listele})

@permission_required('dokumanlar.add_onayli',login_url=onayli_view)
@login_required(login_url=login_view)
def onayli_create(request):
    create20 = onayliForm(request.POST or None, request.FILES or None)
    context = {'create20': create20}
    if request.method == "POST":
        if create20.is_valid():
            a = create20.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('onayli_view')
    return render(request, 'dokumanlar/create14.html', context)

@permission_required('dokumanlar.change_onayli',login_url=onayli_view)
@login_required(login_url=login_view)
def onayli_update(request,pk):
    liste = get_object_or_404(onayli, id=pk)
    create20 = onayliForm(request.POST or None, request.FILES or None, instance=liste)
    if create20.is_valid():
        create20.save()
        return redirect('onayli_view')
    context = {'create20': create20}
    return render(request, 'dokumanlar/create14.html', context)


@permission_required('dokumanlar.delete_onayli',login_url=onayli_view)
@login_required(login_url=login_view)
def onayli_delete(request,pk):
    liste = onayli.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('onayli_view')

@login_required(login_url=login_view)
def isteslim_view(request):
    listele = isteslim.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views15.html', {'listele': listele})


@permission_required('dokumanlar.add_isteslim',login_url=isteslim_view)
@login_required(login_url=login_view)
def isteslim_create(request):
    create21 = isteslimForm(request.POST or None, request.FILES or None)
    context = {'create21': create21}
    if request.method == "POST":
        if create21.is_valid():
            a = create21.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('isteslim_view')
    return render(request, 'dokumanlar/create15.html', context)


@permission_required('dokumanlar.change_isteslim',login_url=isteslim_view)
@login_required(login_url=login_view)
def isteslim_update(request,pk):
    liste = get_object_or_404(isteslim, id=pk)
    create21 = isteslimForm(request.POST or None, request.FILES or None, instance=liste)
    if create21.is_valid():
        create21.save()
        return redirect('isteslim_view')
    context = {'create21': create21}
    return render(request, 'dokumanlar/create15.html', context)


@permission_required('dokumanlar.delete_isteslim',login_url=isteslim_view)
@login_required(login_url=login_view)
def isteslim_delete(request,pk):
    liste = isteslim.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('isteslim_view')

@login_required(login_url=login_view)
def saha_view(request):
    listele = saha.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views16.html', {'listele': listele})


@permission_required('dokumanlar.add_saha',login_url=saha_view)
@login_required(login_url=login_view)
def saha_create(request):
    create22 = sahaForm(request.POST or None, request.FILES or None)
    context = {'create22': create22}
    if request.method == "POST":
        if create22.is_valid():
            a = create22.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('saha_view')
    return render(request, 'dokumanlar/create16.html', context)


@permission_required('dokumanlar.change_saha',login_url=saha_view)
@login_required(login_url=login_view)
def saha_update(request,pk):
    liste = get_object_or_404(saha, id=pk)
    create22 = sahaForm(request.POST or None, request.FILES or None, instance=liste)
    if create22.is_valid():
        create22.save()
        return redirect('saha_view')
    context = {'create22': create22}
    return render(request, 'dokumanlar/create16.html', context)


@permission_required('dokumanlar.delete_saha',login_url=saha_view)
@login_required(login_url=login_view)
def saha_delete(request,pk):
    liste = saha.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('saha_view')

@login_required(login_url=login_view)
def kurul_view(request):
    listele = kurul.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views17.html', {'listele': listele})


@permission_required('dokumanlar.add_kurul',login_url=kurul_view)
@login_required(login_url=login_view)
def kurul_create(request):
    create23 = kurulForm(request.POST or None, request.FILES or None)
    context = {'create23': create23}
    if request.method == "POST":
        if create23.is_valid():
            a = create23.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('kurul_view')
    return render(request, 'dokumanlar/create17.html', context)

@permission_required('dokumanlar.change_kurul',login_url=kurul_view)
@login_required(login_url=login_view)
def kurul_update(request,pk):
    liste = get_object_or_404(kurul, id=pk)
    create23 = kurulForm(request.POST or None, request.FILES or None, instance=liste)
    if create23.is_valid():
        create23.save()
        return redirect('kurul_view')
    context = {'create23': create23}
    return render(request, 'dokumanlar/create17.html', context)

@permission_required('dokumanlar.delete_kurul',login_url=kurul_view)
@login_required(login_url=login_view)
def kurul_delete(request,pk):
    liste = kurul.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('kurul_view')

@login_required(login_url=login_view)
def yonerge_view(request):
    listele = yonerge.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views18.html', {'listele': listele})

@permission_required('dokumanlar.add_yonerge',login_url=yonerge_view)
@login_required(login_url=login_view)
def yonerge_create(request):
    create24 = yonergeForm(request.POST or None, request.FILES or None)
    context = {'create24': create24}
    if request.method == "POST":
        if create24.is_valid():
            a = create24.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('yonerge_view')
    return render(request, 'dokumanlar/create18.html', context)

@permission_required('dokumanlar.change_yonerge',login_url=yonerge_view)
@login_required(login_url=login_view)
def yonerge_update(request,pk):
    liste = get_object_or_404(yonerge, id=pk)
    create24 = yonergeForm(request.POST or None, request.FILES or None, instance=liste)
    if create24.is_valid():
        create24.save()
        return redirect('yonerge_view')
    context = {'create24': create24}
    return render(request, 'dokumanlar/create18.html', context)

@permission_required('dokumanlar.delete_yonerge',login_url=yonerge_view)
@login_required(login_url=login_view)
def yonerge_delete(request,pk):
    liste = yonerge.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('yonerge_view')

@login_required(login_url=login_view)
def ekip_view(request):
    listele = ekip.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views19.html', {'listele': listele})


@permission_required('dokumanlar.add_ekip',login_url=ekip_view)
@login_required(login_url=login_view)
def ekip_create(request):
    create25 = ekipForm(request.POST or None, request.FILES or None)
    context = {'create25': create25}
    if request.method == "POST":
        if create25.is_valid():
            a = create25.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('ekip_view')
    return render(request, 'dokumanlar/create19.html', context)


@permission_required('dokumanlar.change_ekip',login_url=ekip_view)
@login_required(login_url=login_view)
def ekip_update(request,pk):
    liste = get_object_or_404(ekip, id=pk)
    create25 = ekipForm(request.POST or None, request.FILES or None, instance=liste)
    if create25.is_valid():
        create25.save()
        return redirect('ekip_view')
    context = {'create25': create25}
    return render(request, 'dokumanlar/create19.html', context)


@permission_required('dokumanlar.delete_ekip',login_url=ekip_view)
@login_required(login_url=login_view)
def ekip_delete(request,pk):
    liste = ekip.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('ekip_view')

@login_required(login_url=login_view)
def saglik_view(request):
    listele = saglik.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views20.html', {'listele': listele})


@permission_required('dokumanlar.add_saglik',login_url=saglik_view)
@login_required(login_url=login_view)
def saglik_create(request):
    create26 = saglikForm(request.POST or None, request.FILES or None)
    context = {'create26': create26}
    if request.method == "POST":
        if create26.is_valid():
            a = create26.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('saglik_view')
    return render(request, 'dokumanlar/create20.html', context)


@permission_required('dokumanlar.change_saglik',login_url=saglik_view)
@login_required(login_url=login_view)
def saglik_update(request,pk):
    liste = get_object_or_404(saglik, id=pk)
    create26 = saglikForm(request.POST or None, request.FILES or None, instance=liste)
    if create26.is_valid():
        create26.save()
        return redirect('saglik_view')
    context = {'create26': create26}
    return render(request, 'dokumanlar/create20.html', context)

@permission_required('dokumanlar.delete_saglik',login_url=saglik_view)
@login_required(login_url=login_view)
def saglik_delete(request,pk):
    liste = saglik.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('saglik_view')

@login_required(login_url=login_view)
def acil_view(request):
    listele = acil.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views21.html', {'listele': listele})

@permission_required('dokumanlar.add_acil',login_url=acil_view)
@login_required(login_url=login_view)
def acil_create(request):
    create27 = acilForm(request.POST or None, request.FILES or None)
    context = {'create27': create27}
    if request.method == "POST":
        if create27.is_valid():
            a = create27.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('acil_view')
    return render(request, 'dokumanlar/create21.html', context)

@permission_required('dokumanlar.change_acil',login_url=acil_view)
@login_required(login_url=login_view)
def acil_update(request,pk):
    liste = get_object_or_404(acil, id=pk)
    create27 = acilForm(request.POST or None, request.FILES or None, instance=liste)
    if create27.is_valid():
        create27.save()
        return redirect('acil_view')
    context = {'create27': create27}
    return render(request, 'dokumanlar/create21.html', context)

@permission_required('dokumanlar.delete_acil',login_url=acil_view)
@login_required(login_url=login_view)
def acil_delete(request,pk):
    liste = acil.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('acil_view')

@login_required(login_url=login_view)
def diger_view(request):
    listele = diger.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views22.html', {'listele': listele})

@permission_required('dokumanlar.add_diger',login_url=diger_view)
@login_required(login_url=login_view)
def diger_create(request):
    create28 = digerForm(request.POST or None, request.FILES or None)
    context = {'create28': create28}
    if request.method == "POST":
        if create28.is_valid():
            a = create28.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('diger_view')
    return render(request, 'dokumanlar/create22.html', context)

@permission_required('dokumanlar.change_diger',login_url=diger_view)
@login_required(login_url=login_view)
def diger_update(request,pk):
    liste = get_object_or_404(diger, id=pk)
    create28 = digerForm(request.POST or None, request.FILES or None, instance=liste)
    if create28.is_valid():
        create28.save()
        return redirect('diger_view')
    context = {'create28': create28}
    return render(request, 'dokumanlar/create22.html', context)

@permission_required('dokumanlar.delete_diger',login_url=diger_view)
@login_required(login_url=login_view)
def diger_delete(request,pk):
    liste = diger.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('diger_view')

@login_required(login_url=login_view)
def diger2_view(request):
    listele = diger2.objects.all().order_by('pk')
    return render(request , 'dokumanlar/views23.html', {'listele': listele})

@permission_required('dokumanlar.add_diger2',login_url=diger2_view)
@login_required(login_url=login_view)
def diger2_create(request):
    create29 = digerForm2(request.POST or None, request.FILES or None)
    context = {'create29': create29}
    if request.method == "POST":
        if create29.is_valid():
            a = create29.save(commit=False)
            a.Olusturan = request.user
            a.save()
            return redirect('diger2_view')
    return render(request, 'dokumanlar/create23.html', context)

@permission_required('dokumanlar.change_diger2',login_url=diger2_view)
@login_required(login_url=login_view)
def diger2_update(request,pk):
    liste = get_object_or_404(diger2, id=pk)
    create29 = digerForm2(request.POST or None, request.FILES or None, instance=liste)
    if create29.is_valid():
        create29.save()
        return redirect('diger2_view')
    context = {'create29': create29}
    return render(request, 'dokumanlar/create23.html', context)

@permission_required('dokumanlar.delete_diger2',login_url=diger2_view)
@login_required(login_url=login_view)
def diger2_delete(request,pk):
    liste = diger2.objects.get(id=pk)
    #   if User.groups.name('Yetkili'):
    liste.delete()
    context = {'liste': liste}
    return redirect('diger2_view')