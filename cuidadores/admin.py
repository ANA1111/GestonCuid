from django.contrib import admin
from .models import Cuidador

@admin.register(Cuidador)
class CuidadorAdmin(admin.ModelAdmin):
    # Verifique se os nomes aqui batem com o models.py acima
    list_display = ('nome', 'cidade', 'status', 'lista_negra', 'data_cadastro')
    list_filter = ('status', 'lista_negra', 'cidade')
    search_fields = ('nome', 'whatsapp')
    # Comente a linha abaixo se o erro E121 persistir até rodar o migrate
    list_editable = ('status', 'lista_negra')