from django.shortcuts import redirect, render
from sector.models import Sector
from authentication.decorators import admin_required


@admin_required
def sector(request):
    sector = Sector.objects.all()
    data = {
        "sector": sector,
    }
    return render(request, 'sector/sector.html', data)


@admin_required
def addsector(request):
    if request.method == 'POST':
        name = request.POST['name']
        sector = Sector(name=name)
        sector.save()
        return redirect('sector')
    return render(request, 'sector/addsector.html')


@admin_required
def sectordel(request, id):
    sector = Sector(id=id)
    sector.delete()
    return redirect('sector')


def sectoredit(request, id):
    sector1 = Sector.objects.get(id=id)
    data = {
        "sector1": sector1,
    }
    if request.method == "POST":
        name = request.POST['name']
        sector = Sector(id=id, name=name)
        sector.save()
    return render(request, 'sector/edit.html', data)


def sectorupdate(request, id):
    if request.method == "POST":
        name = request.POST['name']
        sector = Sector(id=id, name=name)
        sector.save()
        return redirect('sector')
