from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Publicacion
from .formulario import PublicacionForm

# Create your views here.

def publicacion_lista(request):
    publicaciones =  Publicacion.objects.filter(
        fecha_publicacion__lte=timezone.now()
    ).order_by('fecha_publicacion')
    return render(request, 'articulos/publicacion_lista.html', {"publicaciones":publicaciones})

def publicacion_detalle(request, pk):
    publicacion = get_object_or_404(Publicacion, pk= pk)
    return render(request, 'articulos/publicacion_detalle.html', {'publicacion': publicacion})

def publicacion_nuevo(request):
    if request.method == "POST":
        formulario = PublicacionForm(request.POST)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_creacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm()
        return render(request, 'articulos/publicacion_editar.html', {'formulario': formulario})

def publicacion_editar(request, pk):
    publicacion = get_object_or_404(Publicacion, pk=pk)
    if request.method == "POST":
        formulario = PublicacionForm(request.POST, instance=publicacion)
        if formulario.is_valid():
            publicacion = formulario.save(commit=False)
            publicacion.autor = request.user
            publicacion.fecha_creacion = timezone.now()
            publicacion.save()
            return redirect('publicacion_detalle', pk=publicacion.pk)
    else:
        formulario = PublicacionForm(instance=publicacion)
    return render(request, 'articulos/publicacion_editar.html', {'formulario': formulario})