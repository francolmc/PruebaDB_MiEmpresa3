from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', { 'form': form })

@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)
    return render(request, 'editar_proyecto.html', { 'form': form })

@login_required
def eliminar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'confirmar_eliminar.html', {'proyecto': proyecto})

@login_required
def lista_proyectos(request):
    proyectos = Proyecto.objects.all() # SELECT * FROM proyectos
    return render(request, 'lista_proyectos.html', {'proyectos': proyectos})
