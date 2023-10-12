from django.urls import path
from blog.views import *

urlpatterns = [
    path('', home, name='index'),
    path('juegos_florales/', juegos_florales, name='juegos florales'),
    path('generales/', generales, name='generales'),
    path('concursos/', concursos, name='concursos'),
    path('ferias_escolares/', ferias_escolares, name='ferias escolares'),
    path('<slug:slug>/', detalle_post, name='detalle post'),
]