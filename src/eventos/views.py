from django.shortcuts import render, redirect, get_object_or_404
from .models import EventosDB, OrganizadoresDB
from .forms import EventosForm, OrganizadoresForm
# Create your views here.

def lista_eventos(request):
    eventos = EventosDB.objects.all()
    return render(request, 'eventos/lista_eventos.html', {'eventos': eventos})

def crear_eventos(request):
    if request.method == 'POST':
        form = EventosForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
            form = EventosForm()
    return render(request, "eventos/form_evento.html", {"form": form})


def editar_evento(request, pk):
    evento = get_object_or_404(EventosDB, pk=pk)
    if request.method == 'POST':
        form = EventosForm(request.POST, instance=evento)
        if form.is_valid():
            form.save()
            return redirect('lista_eventos')
    else:
        form = EventosForm(instance=evento)
    return render(request, 'eventos/form_evento.html', {'form': form})


def eliminar_evento(request, pk):
    evento = get_object_or_404(EventosDB, pk=pk)
    if request.method == 'POST':
        evento.delete()
        return redirect('lista_eventos')
    else:
        form = EventosForm(instance=evento)
    return render(request, 'eventos/confirmar_eliminacion.html', {'evento': evento})



def asignar_organizador(request, pk):
    evento = get_object_or_404(EventosDB, pk=pk)
    if request.method == "POST":
        form = OrganizadoresForm(request.POST)
        if form.is_valid():
            organizador = form.save(commit=False)
            organizador.evento = evento
            organizador.save()
            return redirect("lista_eventos")
    else:
        form = OrganizadoresForm()
    return render(request, "eventos/form_organizador.html", {"form": form, "evento": evento})



def toggle_Organizador(request, tarea_id):
    organizador = get_object_or_404(OrganizadoresDB, id=tarea_id)
    organizador.completada = not organizador.completada
    organizador.save()
    return redirect('lista_eventos')



