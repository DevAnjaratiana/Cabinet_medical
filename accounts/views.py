from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .form import InscriptionForm
from django.contrib.auth.forms import AuthenticationForm
from django.views.decorators.cache import never_cache

@never_cache
def inscription(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        form = InscriptionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:connexion')
    else:
        form = InscriptionForm()
    return render(request, 'accounts/inscription.html', {'form': form})

@never_cache
def connexion(request):
    if request.user.is_authenticated:
        return redirect('dashboard:dashboard')
    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('dashboard:dashboard')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/connexion.html', {'form': form})

def deconnexion(request):
    logout(request)
    return redirect('accounts:connexion')