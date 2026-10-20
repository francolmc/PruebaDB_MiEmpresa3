from django.shortcuts import render, redirect, get_object_or_404
from .forms import ProyectoForm
from django.contrib.auth.decorators import login_required
from .models import Proyecto, Categoria
from django.db.models import Q
from django.core.paginator import Paginator
from django.core.exceptions import PermissionDenied

# Create your views here.
def home(request):
    return render(request, 'home.html')

@login_required
def crear_proyecto(request):
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save(commit=False)
            proyecto.usuario = request.user # asignamos el usuario conectado (autenticado)
            proyecto.save()
            proyecto.save_m2m()
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()
    return render(request, 'crear_proyecto.html', { 'form': form })

@login_required
def editar_proyecto(request, pk):
    proyecto = get_object_or_404(Proyecto, pk=pk)
    if proyecto.usuario != request.user:
        raise PermissionDenied
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
    if proyecto.usuario != request.user:
        raise PermissionDenied
    if request.method == 'POST':
        proyecto.delete()
        return redirect('lista_proyectos')
    return render(request, 'confirmar_eliminar.html', {'proyecto': proyecto})

@login_required
def lista_proyectos(request):
    q = request.GET.get('q', '')
    categoria = request.GET.get('categoria', '')

    proyectos = Proyecto.objects.order_by('titulo') # SELECT * FROM proyectos

    if q:
        proyectos = proyectos.filter(
            Q(titulo__icontains=q) | 
            Q(descripcion__icontains=q)
        ) # SELECT * FROM proyectos WHERE titulo LIKE q OR descripcion LIKE q
    if categoria.isdigit():
        proyectos = proyectos.filter(categoria_id=categoria)

    paginator = Paginator(proyectos, 1)
    page_obj = paginator.get_page(request.GET.get('page')) # obtengo el numero de pagina desde la url

    params = request.GET.copy()
    params.pop('page', None)


    return render(request, 'lista_proyectos.html', {
        'proyectos': page_obj,
        'q': q,
        'categorias': Categoria.objects.order_by('nombre'),
        'categoria_id': categoria,
        'querystring': params.urlencode()
        })
