from django.shortcuts import render,redirect
from django.contrib.auth import login,logout,authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users,admin_only

# Create your views here.
def home(request):
    return render(request,'home.html')

@unauthenticated_user
def registerUser(request):
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    if form.is_valid():
        user = form.save()
        username = form.cleaned_data.get('username')

        group, _= Group.objects.get_or_create(name='customer')
        user.groups.add(group)
        messages.success(request, f'Acccount created for {username}. Please login')
        return redirect('login')
    return render(request,'register.html',{'form':form})

@unauthenticated_user
def loginUser(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
           login(request, user)
        return redirect('home')
    messages.error(request, 'Invalid username or password')
    return render(request, 'login.html')

def logoutUser(request):
    logout(request)
    return redirect('login')

@login_required(login_url='login')
@allowed_users(['customer','employee'])
def dashboard(request):
    return render(request,'dashboard.html')

@login_required(login_url='login')
@admin_only
def adminPanel(request):
    return render(request,'admin_panel.html')

@login_required(login_url='login')
@allowed_users(['customer'])
def userPage(request):
    return render(request,'user_page.html')
