from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required

from projects.models import Project
from core.models import ContactMessage

from .forms import LoginForm

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            if user.is_staff:
                return redirect('dashboard')
            else:
                return redirect('home')
    else:
        form = LoginForm()

    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('home')


@staff_member_required
def dashboard_view(request):
    context = {
        "project_count": Project.objects.count(),
        "contact_count": ContactMessage.objects.count(),
    }
    return render(request, 'accounts/dashboard.html', context)