from django.urls import path
from .views import IndexView # O . inciarl em .views indica que eu estou pegando o arquivo do mesmo local desse que estou editando.

urlpatterns = [
    path('inicio/', IndexView.as_view(), name='inicio'),
    #path('endereço de acesso na web/', MinhaView.as_view(), name='nome da url'),
]