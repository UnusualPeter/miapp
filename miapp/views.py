from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from django.utils import timezone

from miapp.models import Notas

# Create your views here.
def home(request):
    notas = Notas.objects.order_by('pub_date').all()

    return render(request, 'miapp/index.html', { 'notas': notas })

def guardar(request):
    texto = request.POST.get('texto')
    fecha = timezone.now()

    Notas.objects.create(texto=texto, pub_date=fecha)

    return HttpResponseRedirect(reverse('miapp:home'))