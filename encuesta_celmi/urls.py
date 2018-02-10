from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from main import urls as EncuestaUrls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(EncuestaUrls)),

]
