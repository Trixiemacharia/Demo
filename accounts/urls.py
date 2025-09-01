from django.urls import path
from . import views

urlpatterns=[
    path('',views.home, name='home'),
    path('login/',views.loginUser, name='login'),
    path('register/',views.registerUser, name='register'),
    path('logout/',views.logoutUser,name='logout'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('admin-panel/',views.adminPanel,name='admin-panel'),
    path('user/',views.userPage,name='user-page'),
]