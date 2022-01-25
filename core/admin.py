from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Acessorio)


def preco_total(self):
    quantidade_dias = abs((self.data_devolucao - self.data_aluguel).days)
    return self.veiculo.preco * 0.001 * quantidade_dias

class aluguel_admin(admin.ModelAdmin):
    list_filter = ('veiculo', )
    list_display = ('cliente', 'data_aluguel', 'data_devolucao', 'veiculo', preco_total)
    field = ((None, {'fields': ('data_aluguel', 'data_devolucao', 'cliente', 'veiculo')}))

class cliente_admin(admin.ModelAdmin):
    list_display = ('nome', 'cpf', 'telefone', )

class veiculo_admin(admin.ModelAdmin):
    list_filter = ('locadora', )
    list_display = ('modelo', 'placa', 'locadora', )


class locadora_admin(admin.ModelAdmin):
    list_display = ('nome', 'cidade', )

admin.site.register(Aluguel, aluguel_admin)
admin.site.register(Cliente, cliente_admin)
admin.site.register(Veiculo, veiculo_admin)
admin.site.register(Locadora, locadora_admin)