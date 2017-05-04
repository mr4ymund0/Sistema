from django.shortcuts import render, redirect
from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from apps.docuamentacion.forms import *
from apps.docuamentacion.models import *

# credenciales
def credenciales_list(request):
	credencial = credenciales.objects.all().order_by('id')
	contexto = {'credenciales':credencial}
	return render(request, 'documentacion/Credenciales/credenciales_list.html', contexto)

def credenciales_view(request):
	if request.method == 'POST':
		form = Credenciales_Form(request.POST)
		if form.is_valid():
			form.save()
		return redirect('documentacion:credencial_listar')
	else:
		form = Credenciales_Form()
		return render(request, 'documentacion/Credenciales/credenciales_form.html', {'form':form})

class credenciales_update(UpdateView):
	model = credenciales
	form_class = Credenciales_Form
	template_name = 'documentacion/Credenciales/credenciales_form.html'
	success_url = reverse_lazy('documentacion:credencial_listar')

class credenciales_delete(DeleteView):
	model = credenciales
	template_name = 'documentacion/Credenciales/credenciales_delete.html'
	success_url = reverse_lazy('documentacion:credencial_listar')

# ficha
class Fichas_list(ListView):
	model = ficha
	template_name = 'documentacion/Fichas/fichas_list.html'
	paginate_by = 5

class Fichas_view(CreateView):
	model = ficha
	form_class = Ficha_Form
	template_name = 'documentacion/Fichas/fichas_form.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

class Fichas_update(UpdateView):
	model = ficha
	form_class = Ficha_Form
	template_name = 'documentacion/Fichas/fichas_form.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

class Fichas_delete(DeleteView):
	model = ficha
	template_name = 'documentacion/Fichas/fichas_delete.html'
	success_url = reverse_lazy('documentacion:ficha_listar')

# equipo_ficha
class Equipo_Fichas_list(ListView):
	model = equipo_ficha
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_list.html'
	paginate_by = 2

class  Equipo_Fichas_view(CreateView):
	model = equipo_ficha
	form_class = Equipo_Ficha_Form
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_form.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

class  Equipo_Fichas_update(UpdateView):
	model = equipo_ficha
	form_class = Equipo_Ficha_Form
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_form.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

class Equipo_Fichas_delete(DeleteView):
	model = equipo_ficha
	template_name = 'documentacion/Equipo Ficha/equipo_ficha_delete.html'
	success_url = reverse_lazy('documentacion:equipo_ficha_listar')

# ficha_cat_tecnologias
def ficha_cat_tecnologias_list(request):
	ficha_tec = ficha_cat_tecnologias.objects.all().order_by('id')
	contexto = {'ficha_tecno': ficha_tec}
	return render(request, 'documentacion/Ficha Tecnologias/ficha_tecnologia_list.html', contexto)

# documento_archivo
def documento_archivo_list(request):
	documento = documento_archivo.objects.all().order_by('id')
	contexto = {'documentos': documento}
	return render(request, 'documentacion/Documentos/documento_list.html', contexto)

# logtable