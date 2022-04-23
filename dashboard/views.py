from django.shortcuts import render
from authentication.models import Org, Client

# @


def dashboard(request):
    org = Org.objects.all().count()
    client = Client.objects.all().count()
    data = {
        'org': org,
        'client': client
    }
    return render(request, 'dashboard/dashboard.html', data)


def org_portal(request):
    return render(request, 'dashboard/org_portal.html')


def client_portal(request):
    return render(request, 'dashboard/client_portal.html')
