from django.shortcuts import render, redirect
from authentication.models import Org, Client, User
from authentication.decorators import admin_required, org_required, client_required
from django.contrib.auth.decorators import login_required
# @


@admin_required
def dashboard(request):
    org = Org.objects.all().count()
    client = Client.objects.all().count()
    data = {
        'org': org,
        'client': client
    }
    return render(request, 'dashboard/dashboard.html', data)


@org_required
def org_portal(request):
    return render(request, 'dashboard/org_portal.html')


@client_required
def client_portal(request):
    return render(request, 'dashboard/client_portal.html')


@admin_required
def user(request):
    user = User.objects.all()
    data = {
        'user': user,
    }
    return render(request, 'user/user.html', data)


@admin_required
def user_delete(request, id):
    user = User.objects.get(id=id)
    user.delete()
    return redirect('user')


@admin_required
def user_edit(request, id):
    user1 = User.objects.get(id=id)
    data = {
        'user1': user1
    }
    if request.method == "POST":
        super = request.POST['super']
    return render(request, 'user/edit.html', data)


@admin_required
def user_update(request, id):
    if request.method == "POST":
        super = request.POST['super']
        user = User(id=id)
        user.is_active = True
        user.is_staff = True
        user.is_staff = True
        user.save()
        return redirect('user')


@org_required
def orgclient(request):
    client = Client.objects.filter(org__user_id=request.user.id)
    data = {
        "client": client,
    }
    return render(request, 'dashboard/orgclient.html', data)
