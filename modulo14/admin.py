from django.contrib import admin
from modulo14.models import Produto

@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'preco', 'quantidade')
    search_fields = ('nome',)
    list_filter = ('preco',)