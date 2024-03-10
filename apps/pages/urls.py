from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home'),
    # Exemplo de padrão de URL
    # path('apagar/<int:id>/', views.apagar_consulente, name='apagar_consulente'),
    # path('atualizar/<int:id>/', views.atualizar_consulente, name='atualizar_consulente'),
    path('ver/<int:id>/', views.ver_consulente, name='ver_consulente'),

]