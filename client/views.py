from django.shortcuts import render, redirect
from authentication.models import User, Client
from authentication.models import Org
import uuid
from client.helpers import send_password_mail, send_success_mail
from django.contrib.auth.decorators import login_required
from authentication.decorators import admin_required


@admin_required
def client(request):
    client = Client.objects.all()
    data = {
        'client': client,
    }
    return render(request, 'client/client.html', data)


@admin_required
def addclient(request):
    org1 = Org.objects.all()
    data = {
        'org1': org1,
    }
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        org = request.POST['org']
        location = request.POST['location']
        size = request.POST['size']
        crop_types = request.POST['crop_types']
        irrigation = request.POST['irrigation']
        user = User(
            first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.is_client = True
        user.save()
        client = Client(user=user)
        client.org_id = org
        client.location = location
        client.size = size
        client.crop_types = crop_types
        client.irrigation = irrigation
        token = str(uuid.uuid4())
        client.p_token = token
        client.save()
        # print(first_name, last_name, username, email, password,
        #       org, location, size, crop_types, irrigation)
        send_password_mail(user.email, token, user)
        return redirect('client')
    return render(request, 'client/addclient.html', data)


def clientactivate(request, token):
    context = {}
    try:
        org_obj = Client.objects.get(p_token=token)
        context = {'user_id': org_obj}

    except Exception as e:
        print(e)
    return render(request, 'clientmail/activated.html', context)


def clientactivated(request):
    if request.method == "POST":
        password = request.POST['password']
        cpassword = request.POST['cpassword']
        user_id = request.POST['user_id']
        if password == cpassword:
            user = User.objects.get(id=user_id)
            user.set_password(password)
            user.is_active = True
            user.save()
            send_success_mail(user.email, user)
            return redirect('login')
        else:
            # messages.error(request, 'Password not match')
            return redirect('login')
    else:
        return render(request, 'clientmail/activated.html')


@admin_required
def client_delete(request, id):
    client = User.objects.get(pk=id)
    client.delete()
    return redirect('client')


@admin_required
def client_edit(request, id):
    client1 = Client.objects.get(pk=id)
    data = {
        'client1': client1,
    }
    return render(request, 'client/edit.html', data)


@admin_required
def client_update(request, id):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        org = request.POST['org']
        p_token = request.POST['p_token']
        location = request.POST['location']
        size = request.POST['size']
        crop_types = request.POST['crop_types']
        irrigation = request.POST['irrigation']
        user = User(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.is_active = True
        user.is_client = True
        user.password = password
        user.save()
        clin = Client(user=user)
        # clin.user.first_name = first_name
        # clin.user.last_name = last_name
        # clin.user.email = email
        clin.org_id = org
        clin.location = location
        clin.size = size
        clin.p_token = p_token
        clin.crop_types = crop_types
        clin.irrigation = irrigation
        clin.save()
        return redirect("client")
