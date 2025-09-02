
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reserva

def lista_reservas(request):
    reservas = Reserva.objects.all().order_by('-fecha')  # Ordena por fecha descendente
    return render(request, 'restaurante/lista.html', {'reservas': reservas})

def nueva_reserva(request):
    if request.method == 'POST':
        nombre_cliente = request.POST.get('nombre_cliente')
        fecha = request.POST.get('fecha')
        hora = request.POST.get('hora')
        personas = request.POST.get('personas')
        reserva = Reserva(nombre_cliente=nombre_cliente, fecha=fecha, hora=hora, personas=personas)
        reserva.save()
        return redirect('lista_reservas')
    return render(request, 'restaurante/nueva.html')

def cancelar_reserva(request, id):
    reserva = get_object_or_404(Reserva, id=id)
    reserva.delete()
    return redirect('lista_reservas')
