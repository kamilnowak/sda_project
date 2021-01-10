from django.shortcuts import render, redirect

# Create your views here.
from users.forms import UserRegisterForm


def register(request):
    if request.method == 'GET':
        form = UserRegisterForm
        return render(request, 'registration/register.html', {"form": form})
    elif request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
