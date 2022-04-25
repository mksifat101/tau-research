from django.shortcuts import redirect, render
from sector.models import Sector
from authentication.models import User, Org
import uuid
from authentication.helpers import send_password_mail, send_success_mail
from authentication.decorators import admin_required


@admin_required
def organisation(request):
    org = Org.objects.all()
    data = {
        'org': org,
    }
    return render(request, 'organisation/organisation.html', data)


@admin_required
def addorg(request):
    sector1 = Sector.objects.all()
    data = {
        'sector1': sector1,
    }
    if request.method == "POST":
        org_name = request.POST['org_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        sector = request.POST['sector']
        user = User(
            first_name=first_name, last_name=last_name, username=username, email=email)
        user.set_password(password)
        user.is_org = True
        user.save()
        org = Org(user=user)
        org.org_name = org_name
        org.sector_id = sector
        token = str(uuid.uuid4())
        org.p_token = token
        org.save()
        send_password_mail(user.email, token, user)
        return redirect('organisation')
    return render(request, 'organisation/addorg.html', data)


def activate(request, token):
    context = {}
    try:
        org_obj = Org.objects.get(p_token=token)
        context = {'user_id': org_obj}

    except Exception as e:
        print(e)
    return render(request, 'orgmail/activated.html', context)


def activated(request):
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
        return render(request, 'orgmail/activated.html')


@admin_required
def org_delete(request, id):
    org = User.objects.get(id=id)
    org.delete()
    return redirect('organisation')


def org_edit(request, id):
    org1 = Org.objects.get(pk=id)
    data = {
        'org1': org1,
    }
    return render(request, 'organisation/edit.html', data)


def org_update(request, id):
    if request.method == "POST":
        org_name = request.POST['org_name']
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        sector = request.POST['sector']
        p_token = request.POST['p_token']
        user = User(id=id)
        user.first_name = first_name
        user.last_name = last_name
        user.username = username
        user.email = email
        user.password = password
        user.is_org = True
        user.is_active = True
        user.save()
        org = Org(user=user)
        org.org_name = org_name
        org.sector_id = sector
        org.p_token = p_token
        org.save()
        return redirect('organisation')
