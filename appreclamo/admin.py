from django.contrib import admin
from django.contrib.auth.models import Group

from appreclamo.models import Clientes, Articulos, Pedidos, Viajero,Reserva, Pagos, Reparticion, Reclamos, Agentes,Empleados,Funcion,Sitlab,Anuncios
     

# Register your models here.


class ClientesAdmin(admin.ModelAdmin):
    list_display=("nombre", "direccion", "email", "tfno")

    #agrago un buscador
    search_fields=("nombre", "tfno")

class Articulosadmin(admin.ModelAdmin):
    #para hacer filtrado
    list_filter=("seccion",)

class PedidosAdmin(admin.ModelAdmin):
    list_display=("numero", "fecha", "entregado")
    list_filter=("fecha",)
    date_hierarchy=("fecha")

class ReservaInline(admin.StackedInline):
    model = Reserva
    extra = 0  
    

class PagoInline(admin.StackedInline):
    model = Pagos
    extra = 0  


    # nuevo codigo
class ViajeroAdmin(admin.ModelAdmin):
    list_display=("apellido", "nombre", "direccion", "telefono")
    #inlines = [ReservaInline]
    inlines = (ReservaInline,PagoInline)
    #inlines = (PagoInline, )
    search_fields=("apellido", "nombre")
    #list_filter=("apellido",)


    

class ReparticionAdmin(admin.ModelAdmin):
    model = Reparticion
    
    ordering = ['nombre']    
    list_display=("nombre", "ubicacion", "telefono")
    #search_fields=("nombre",)
    #list_filter=("fecha_reserva",)

class AgenteAdmin(admin.ModelAdmin):
    model = Agentes
    
    list_display=("nombre", "funcion", "observacion")
    search_fields=("nombre",)
    #list_filter=("fecha_reserva",)

    
class ReclamoAdmin(admin.ModelAdmin):
    
    #model = Reclamos
    search_fields=("motivo","cod_repart__nombre",)
    list_filter=("Fecha_reclamo","estadia_reclamo",)    
    date_hierarchy=("Fecha_reclamo")
    list_display = ['Fecha_reclamo', 'cod_repart','motivo','Pedido_por','estadia_reclamo','cod_agente','prioridad_reclamo',]
    #autocomplete_fields = ['nombre']

class PagosAdmin(admin.ModelAdmin):
    model = Viajero
    #list_display=("fecha_reserva", "cabana")
    #list_display=("fecha_reserva", "cabana", "get_nombre")
    list_display=("fecha_pago", "monto", "get_nombre")
    list_filter=("fecha_pago",)
    search_fields=("viajero__apellido",)

    def get_nombre(self, obj):
        return obj.viajero.apellido
    get_nombre.short_description = 'Viajero'
    get_nombre.admin_order_field = 'nombre viajero '


class ReservaAdmin(admin.ModelAdmin):
    model = Viajero
    #list_display=("fecha_reserva", "cabana")
    #list_display=("fecha_reserva", "cabana", "get_nombre")
    list_display=("fecha_reserva", "cabana", "get_nombre")
    list_filter=("fecha_reserva",)

    def get_nombre(self, obj):
        return obj.viajero.nombre
    get_nombre.short_description = 'Viajero'
    get_nombre.admin_order_field = 'nombre viajero '


class EmpleadosAdmin(admin.ModelAdmin):
    
    #model = Reclamos
    search_fields=("nombre",)
    list_filter=("cod_func","cod_sitlab","turno",)        
    #date_hierarchy=("Fecha_reclamo")
    list_display = ['nombre' ,'numdoc' ,'cod_func','turno','cod_sitlab','Fecha_nac','cuil',]



class FuncionAdmin(admin.ModelAdmin):     
    list_display = ['nombre' ,]
  
    
#     #list_filter=("Fecha_reclamo","estadia_reclamo",)    
#     #date_hierarchy=("Fecha_reclamo")



class SitlabAdmin(admin.ModelAdmin):
    list_display = ['nombre' ,]
#     #model = Reclamos
#     search_fields=("nombre",)
#     #list_filter=("Fecha_reclamo","estadia_reclamo",)    
#     #date_hierarchy=("Fecha_reclamo")
#     list_display = ['Nombre' ,]


# fin nuevo codigo


#admin.site.register(Clientes,ClientesAdmin)
#admin.site.register(Articulos,Articulosadmin)
#admin.site.register(Pedidos,PedidosAdmin)
#admin.site.register(Viajero,ViajeroAdmin)
#admin.site.register(Pagos,PagosAdmin)
admin.site.register(Anuncios)
admin.site.register(Reclamos,ReclamoAdmin)
admin.site.register(Agentes,AgenteAdmin)


# nuevo

#admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Reparticion,ReparticionAdmin)
admin.site.register(Empleados,EmpleadosAdmin)
admin.site.register(Funcion,FuncionAdmin)
admin.site.register(Sitlab,SitlabAdmin)




# fin nuevo
admin.site.site_header = "SISTEMA DE RECLAMOS" 