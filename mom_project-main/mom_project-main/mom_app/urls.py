from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view, name='login'),              # login page
    path('logout/', views.logout_view, name='logout'),     # logout
    path('moms/', views.mom_list, name='mom_list'),        # MoM list
    path('moms/create/', views.mom_create, name='mom_create'),  # create MoM
]
