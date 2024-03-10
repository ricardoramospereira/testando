from django.contrib import admin
from .models import Consulente

# Opção 1: Registro simples do modelo
# admin.site.register(Consulente)

# Opção 2: Personalizando a interface do admin
class ConsulenteAdmin(admin.ModelAdmin):
    list_display = ('nome', 'data_cadastro', 'observacoes')  # Campos que você quer mostrar na listagem
    search_fields = ('nome',)  # Campos pelos quais você quer permitir a pesquisa
    list_filter = ('data_cadastro',)  # Campos pelos quais você quer permitir filtros

# Descomente a linha abaixo se optar pela personalização
admin.site.register(Consulente, ConsulenteAdmin)

