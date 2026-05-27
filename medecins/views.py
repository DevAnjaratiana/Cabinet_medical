from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django import forms
from .models import Medecin

# ==================== FORMULAIRE ====================

class MedecinForm(forms.ModelForm):
    class Meta:
        model = Medecin
        fields = ['nom', 'prenom', 'specialite', 'telephone', 'email']  
        widgets = {
            'nom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le nom'}),
            'prenom': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Entrez le prénom'}),
            'specialite': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: Cardiologue, Généraliste'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Ex: 06 12 34 56 78'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Ex: docteur@email.com'}),
        }
        labels = {
            'nom': 'Nom ',
            'prenom': 'Prénom',
            'specialite': 'Spécialité ',
            'telephone': 'téléphone',
            'email': 'email',
        }
# ==================== CRUD MEDECIN ====================

def medecin_list(request):
    """Display all doctors"""
    medecins = Medecin.objects.all().order_by('nom', 'prenom')
    return render(request, 'medecins/medecin_list.html', {'medecins': medecins})

def medecin_create(request):
    """Add a new doctor"""
    if request.method == 'POST':
        form = MedecinForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docteur ajouté avec succès!')
            return redirect('medecins:medecin_list')
        else:
            print("Form errors:", form.errors)
    else:
        form = MedecinForm()
    return render(request, 'medecins/medecin_form.html', {'form': form, 'title': 'Add Doctor'})

def medecin_update(request, pk):
    """Modify an existing doctor"""
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        form = MedecinForm(request.POST, instance=medecin)
        if form.is_valid():
            form.save()
            messages.success(request, 'Docteur  modifié avec succès!')
            return redirect('medecins:medecin_list')
    else:
        form = MedecinForm(instance=medecin)
    return render(request, 'medecins/medecin_form.html', {'form': form, 'title': 'Edit Doctor'})

def medecin_delete(request, pk):
    """Delete a doctor"""
    medecin = get_object_or_404(Medecin, pk=pk)
    if request.method == 'POST':
        medecin.delete()
        messages.success(request, 'Doctor supprimé avec succès!')
        return redirect('medecins:medecin_list')
    return render(request, 'medecins/medecin_confirm_delete.html', {'medecin': medecin})

def medecin_detail(request, pk):
    """Display doctor details"""
    medecin = get_object_or_404(Medecin, pk=pk)
    return render(request, 'medecins/medecin_detail.html', {'medecin': medecin})