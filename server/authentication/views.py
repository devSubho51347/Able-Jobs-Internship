from django.shortcuts import render
from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
# Create your views here.


def login_page(request):
    context = {}
    if request.user.is_authenticated:

        return render(request,'authentication/login_page.html', context)

    else:
        if request.method == 'POST':
            username = request.POST.get('Username')
            password = request.POST.get('Password')
            user = authenticate(request, username = username, password = password)

            if  user is not None:
                login(request,user)
                return render(request,'authentication/login_page.html', context )

    return render(request, 'authentication/login_page.html', context)


## Method for logout functionality

def logout_page(request):
    logout(request)
    return redirect('login')

