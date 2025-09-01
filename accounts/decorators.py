from django.http import HttpResponse
from django.shortcuts import render,redirect

def unauthenticated_user(view_func):
    def wrapper(request, *args, **kwargs):
        if request.user.is_authenticated:
            return redirect('home')
        return view_func(request,*args,**kwargs)
    return wrapper

def allowed_users(allowed_roles=[]):
    def decorator(view_func):
        def wrapper(request,*args,**kwargs):
            group = None #assumes that users belong to no group at first
            if request.user.groups.exists():
                group=request.users.groups.all()[0].name

                if group in allowed_roles:
                    return view_func(request,*args,**kwargs)
                else:
                    return HttpResponse("you are not authorized")
        return wrapper
    return decorator

def admin_only(view_func):
    def wrapper_function(request, *args, **kwargs):
        if group =='customer':
         return redirect('userpage')
        
        if group == 'admin':
            return view_func(request,*args,**kwargs)
        return wrapper_function
