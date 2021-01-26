"""tiendaonline URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf.urls import url 

from appreclamo import views
#from gestionpedidos.views import web_viajero,web_visitante


from django.conf import settings
from django.conf.urls.static import static
#from django.urls import path # nuevo se puede sacar


# from gestionpedidos.views import (
#     web_viajero_pago

# )

urlpatterns = [
    path('admin/', admin.site.urls),
    path('lanuncio/', views.anuncio,name='lanuncio'), 
    path('reclam/', views.web_reclamos,name='lireclamo'), 
    path('listarRecpen/', views.reclamopen, name='listarRecpen'),
    path('listarRecrea/', views.reclamorea, name='listarRecrea'),
    #path('listarReclamos/', views.ListarReclamos.as_view(), name='listarReclamos'),
    path('listarReclamos/', views.ListarReclamos, name='listarReclamos'),
    #path('listarReclamos/generarReclamoPDF/<int:p>',views.GenerarReclamoPDF.as_view(), name='generarReclamoPDF'),
    path('reclam/generarReclamoPDF/<int:p>',views.GenerarReclamoPDF, name='generarReclamoPDF'),    
    path('lista/', views.web_viajero),
    path('listav/', views.web_visitante),
    path('listapa/', views.web_viajero_pago),
    path('', views.index, name='index'),
    #path('',views.index), ### nuevoooo
    re_path(r'^index/$', views.index, name='index'),
    re_path(r'^palista/$', views.web_viajero_pago, name='listpag'),
    re_path(r'^admin/$', views.web_viajero_pago, name='admi'),
    re_path(r'^genre/$', views.GenerarReclamoPDF, name='recl'),
    #path('crearp/', views.CrearPedidos),
    #path('listomip/', views.Listar_Pedido),    
    #re_path(r'^editped/(?P<id>\d+)/$', views.Editar_Pedidos, name='editoped'),
    #re_path(r'^elimPed/(?P<id>\d+)/$', views.Eliminar_Pedidos, name="elipedido"),
    #re_path(r'˄gestionpedidos/',include('gestionpedidos.urls')),
    #path('inicio/', include('gestionpedidos.urls')),
] +static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

"""
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
"""