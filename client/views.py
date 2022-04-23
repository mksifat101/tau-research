from django.shortcuts import render


def client(request):
    return render(request, 'client/client.html')


def addclient(request):
    return render(request, 'client/addclient.html')
