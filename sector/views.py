from django.shortcuts import redirect, render
from sector.models import Sector


def sector(request):
    sector = Sector.objects.all()
    data = {
        "sector": sector,
    }
    return render(request, 'sector/sector.html', data)


def addsector(request):
    if request.method == 'POST':
        name = request.POST['name']
        sector = Sector(name=name)
        sector.save()
        return redirect('sector')
    return render(request, 'sector/addsector.html')


def sectordel(request, id):
    sector = Sector(id=id)
    sector.delete()
    return redirect('sector')
