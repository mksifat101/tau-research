from django.shortcuts import render, redirect, HttpResponse
from django.contrib import auth


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            # messages.success(request, 'Login Successfull')
            # return redirect('dashboard')
            if user.is_org:
                return redirect('org_portal')
            elif user.is_client:
                return redirect('client_portal')
            elif user.is_superuser:
                return redirect('dashboard')
            else:
                return redirect('dashboard')
            url = request.META.get('HTTP_REFERER')
        else:
            # messages.error(request, 'Invalid login crisidals')
            return redirect('login')
    return render(request, 'authentication/login.html')


def logout(request):
    auth.logout(request)
    return redirect('login')
