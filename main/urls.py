from django.conf.urls import url
from django.urls import path, include
from . import views


urlpatterns = [
	path('', views.EncuestaView.as_view(), name='Encuesta'),
	path('gracias/', views.GraciasView.as_view(),name="gracias")

	]
