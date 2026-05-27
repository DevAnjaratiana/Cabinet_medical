from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from rendezvous.models import RendezVous
from .models import Consultation
from .form import ConsultationForm

def liste(request):
    consultations = Consultation.objects.select_related('rendez_vous__patient', 'rendez_vous__medecin').all()
    return render(request, 'consultations/consultation_list.html', {'consultations': consultations})

def detail(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    return render(request, 'consultations/consultation_detail.html', {'consultation': consultation})

def create(request):
    if request.method == 'POST':
        form = ConsultationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consultation ajoutée avec succès.')
            return redirect('consultations:liste')
    else:
        form = ConsultationForm()
    
    return render(request, 'consultations/consultation_form.html', {
        'form': form,
        'title': 'Nouvelle consultation'
    })

def update(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        form = ConsultationForm(request.POST, instance=consultation)
        if form.is_valid():
            form.save()
            messages.success(request, 'Consultation modifiée avec succès.')
            return redirect('consultations:liste')
    else:
        form = ConsultationForm(instance=consultation)
    
    return render(request, 'consultations/consultation_form.html', {
        'form': form,
        'consultation': consultation,
        'title': 'Modifier la consultation'
    })

def delete(request, pk):
    consultation = get_object_or_404(Consultation, pk=pk)
    if request.method == 'POST':
        consultation.delete()
        messages.success(request, 'Consultation supprimée avec succès.')
        return redirect('consultations:liste')
    
    return render(request, 'consultations/consultation_confirm_delete.html', {'consultation': consultation})