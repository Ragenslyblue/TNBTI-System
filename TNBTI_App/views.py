from django.contrib.auth import logout
from django.contrib.auth.models import auth
from django.shortcuts import render, redirect
from .forms import UserForm
from .models import RegisterUser
from django.contrib.auth.decorators import login_required

# Create your views here.

def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            print('Username OR password does not exit')
            return redirect('login')

    else:
        return render(request, 'login.html')


def logoutUser(request):
    logout(request)
    return redirect('login')


@login_required(login_url='login')
def homePage(request):
    return render(request, 'home.html')


@login_required(login_url='login')
def manageUser(request):
    forms = UserForm()
    users = RegisterUser.objects.all()

    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()

    context = {
        'forms': forms,
        'users': users,
    }
    return render(request, 'manage-user.html', context)


@login_required(login_url='login')
def deleteUser(request, pk):
    user = RegisterUser.objects.get(id=pk)
    user.delete()

    return redirect(manageUser)
