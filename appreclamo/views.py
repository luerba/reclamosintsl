from django.shortcuts import render, redirect
from appreclamo.models import Viajero, Reserva, Pedidos, Pagos, Reclamos, Anuncios # agrege pedidos
#from my_app import views
from django.db.models import Q
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from appreclamo.funciones import render_to_pdf
from django.http import HttpResponseRedirect, HttpResponse,FileResponse
from django.contrib.auth import authenticate, login, logout
#from .reportePDF import reportePDF

#from .forms import PedidosForm # agregado


# Create your views here.

# codigo anterior

# codigo nuevo

 
#class GenerarReclamoPDF(View):
#class GenerarReclamoPDF(View):
    #login_url = 'login'
    #redirect_field_name = None

def GenerarReclamoPDF(self,p):
        import io
        from reportlab.pdfgen import canvas
        import datetime

        reclamo = Reclamos.objects.get(id=p)
        #general = Opciones.objects.get(id=1)
        #detalles = DetalleFactura.objects.filter(id_factura_id=p)          

        data = {
            'fecha_reclamo': reclamo.Fecha_reclamo, 
            'id_reclamo': reclamo.id,
            'solicitante': reclamo.Pedido_por,
            'telefono': reclamo.cod_repart.telefono, 
            'Nombre_reparticion': reclamo.cod_repart.nombre,
            'motivo': reclamo.motivo,
            'id_reporte': reclamo.id,
            'trabajado_por': reclamo.cod_agente.nombre,
            'observacion': reclamo.observacion,
            'modo': 'reclamos',
            #'general':general
        }

        nombre_reclamo = "Reclamo_%s.pdf" % (reclamo.id)

        pdf = render_to_pdf('reclamo/pdf/reclamo.html', data)
        response = HttpResponse(pdf,content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="%s"' % nombre_reclamo

        return response  


# class ListarReclamos(LoginRequiredMixin, View):
#     login_url = 'login'
#     redirect_field_name = None    

#     def get(self, request):

        
#         reclamos = Reclamos.objects.all()
        
#         #Envia al usuario el formulario para que lo llene
#         contexto = {'tabla':reclamos,'dire':"generarReclamoPDF"}   
#         #contexto = complementarContexto(contexto,request.user)
#         return render(request, 'listarReclamos.html', contexto)  
#         #return render(request, 'listar_Reclamos.html', contexto)

#     def post(self, request):
#         pass        


    

def web_viajero(request):
    #list_via = Viajero.objects.all()
    list_res = Reserva.objects.select_related('viajero').all()
    return render(request, "Lista_viajero.html", locals())
    
def web_viajero_pago(request):
    #list_via = Viajero.objects.all()
    list_pag = Pagos.objects.select_related('viajero').all()
    return render(request, "Lista_via_pago.html", locals())

def web_visitante(request):
    list_via = Viajero.objects.all()
    return render(request, "Lista_visita.html", locals())

def web_reclamos(request):
    list_rec = Reclamos.objects.all().order_by('-Fecha_reclamo')                
    return render(request, "Lista_reclamos.html", locals())
    

def ListarReclamos(request):
    list_rec = Reclamos.objects.all()
    return render(request, "ListarReclamos.html", locals())


# def GenerarReclamoPDF(self, request, p):
#     import io
#     from reportlab.pdfgen import canvas
#     import datetime

#     reclamo = Reclamos.objects.get(id=p)
    
#     data = {
#         'fecha_reclamo': reclamo.Fecha_reclamo, 
#         'id_reclamo': reclamo.id,
#         'solicitante': reclamo.Pedido_por,
#         'telefono': reclamo.cod_repart.telefono, 
#         'Nombre_reparticion': reclamo.cod_repart.nombre,
#         'motivo': reclamo.motivo,
#         'id_reporte': reclamo.id,
#         'trabajado_por': reclamo.cod_agente.nombre,
#         'observacion': reclamo.observacion,
#         'modo': 'reclamos',
#          #'general':general
#         }

#     nombre_reclamo = "Reclamo_%s.pdf" % (reclamo.id)

#     pdf = render_to_pdf('gestionpedidos/pdf/reclamo.html', data)
#     response = HttpResponse(pdf,content_type='application/pdf')
#     response['Content-Disposition'] = 'attachment; filename="%s"' % nombre_reclamo

#     return response  

    # list_rec = Reclamos.objects.all()
    # return render(request, "ListarReclamos.html", locals())

# fun codigo nuevo




def index(request):
    
    list_rec = Reclamos.objects.all().order_by('-Fecha_reclamo') 
            
    return render(request,"index.html", locals())


def anuncio(request):
    
    list_rec = Anuncios.objects.all().order_by('-Fecha_anuncio') 
            
    return render(request,"anuncio.html", locals())




def reclamopen(request):
    
    list_rec_pen = Reclamos.objects.filter(estadia_reclamo='2') 
            
    return render(request,"listarecpen.html", locals())

def reclamorea(request):
    
    list_rec_rea = Reclamos.objects.filter(estadia_reclamo='1') 
            
    return render(request,"listarecrea.html", locals())