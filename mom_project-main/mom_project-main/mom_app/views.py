from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .models import MoM, User
from django.contrib.auth.decorators import login_required

# Login view
def login_view(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('mom_list')
        else:
            return render(request, 'login.html', {'error':'Invalid credentials'})
    return render(request, 'login.html')

# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')

# MoM list view with role-based visibility
@login_required
def mom_list(request):
    user_role_order = {
        'faculty': 1,
        'course_coordinator': 2,
        'module_coordinator': 3,
        'pac': 4,
        'dfb': 5,
        'cdc': 6
    }
    current_level = user_role_order[request.user.role]
    moms = MoM.objects.filter(
        created_by__role__in=[role for role, order in user_role_order.items() if order <= current_level]
    ).order_by('-date')
    return render(request, 'mom_list.html', {'moms': moms})

# MoM create view
@login_required
def mom_create(request):
    if request.method == "POST":
        subject = request.POST['subject']
        agenda = request.POST['agenda']
        discussion = request.POST['discussion']
        action_items = request.POST['action_items']
        MoM.objects.create(
            subject=subject,
            agenda=agenda,
            discussion=discussion,
            action_items=action_items,
            created_by=request.user
        )
        return redirect('mom_list')
    return render(request, 'mom_create.html')
