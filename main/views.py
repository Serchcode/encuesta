from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import View
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .forms import EncuestaForm
from django.contrib import messages
from django.shortcuts import get_object_or_404

class EncuestaView(View):

	template_name = "encuesta.html"

	def get(self, request):
		form = EncuestaForm()
		context = {'form':form}
		return render(request,self.template_name,context)

	def post(self, request):
		if request.method == "POST":	
			form = EncuestaForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('gracias')
		else:
			print(form.errors)
			context ={
				'form':form,
				}
			return HttpResponse('No se pudo enviar la encuesta')

class GraciasView(View):
	def get(self, request):
		template_name="gracias.html"
		return render(request, template_name)