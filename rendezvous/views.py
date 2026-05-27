from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import RendezVous
from .form import RendezVousForm

def liste(request):
    rdvs = RendezVous.objects.select_related('patient', 'medecin').all()
    return render(request, 'rendezvous/rendezvous_list.html', {'rdvs': rdvs})

def ajouter(request):
    if request.method == 'POST':
        form = RendezVousForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'RDV ajouté ✅')
            return redirect('rendezvous:liste')
    else:
        form = RendezVousForm()
    return render(request, 'rendezvous/rendezvous_form.html', {'form': form})

def modifier(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        form = RendezVousForm(request.POST, instance=rdv)
        if form.is_valid():
            form.save()
            messages.success(request, 'RDV modifié ✅')
            return redirect('rendezvous:liste')
    else:
        form = RendezVousForm(instance=rdv)
    return render(request, 'rendezvous/rendezvous_form.html', {'form': form})

def supprimer(request, pk):
    rdv = get_object_or_404(RendezVous, pk=pk)
    if request.method == 'POST':
        rdv.delete()
        messages.success(request, 'RDV supprimé ❌')
        return redirect('rendezvous:liste')
    return render(request, 'rendezvous/rendezvous_confirm_delete.html', {'rdv': rdv})