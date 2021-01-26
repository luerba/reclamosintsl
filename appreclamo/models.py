from django.db import models
from datetime import datetime
from django.utils import timezone

# Create your models here.
# por cada tabla una clase


class Anuncios(models.Model):
    Fecha_anuncio = models.DateField(null=False)
    Titulo = models.CharField(max_length=50, blank=True)
    Mensaje1 = models.CharField(max_length=150,null=True)
    Mensaje2 = models.CharField(max_length=150,blank=True)
    Mensaje3 = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.Titulo



class Sitlab(models.Model):
    nombre = models.CharField(max_length=50, null=True,unique=True)
    observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.nombre


class Funcion(models.Model):
    nombre = models.CharField(max_length=70, null=True,unique=True)
    observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.nombre

class Empleados(models.Model):
    nombre = models.CharField(max_length=80, blank=False)
    numdoc = models.CharField(max_length=12, blank=False)
    domicilio = models.CharField(max_length=80, blank=True)    
    cod_func = models.ForeignKey(Funcion,to_field='nombre', on_delete=models.CASCADE)
    telef = models.CharField(max_length=12, blank=True)
    turno = models.CharField(max_length=30, blank=True)
    cuil = models.CharField(max_length=12, blank=True)
    cod_sitlab = models.ForeignKey(Sitlab,to_field='nombre', on_delete=models.CASCADE)
    Fecha_nac = models.DateField(null=True)
    observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.nombre








class Reparticion(models.Model):
    #id
    nombre = models.CharField(max_length=60, null=True,unique=True)
    ubicacion = models.CharField(max_length=60, null=True)
    telefono = models.CharField(max_length=50, null=True)    
    encargado = models.CharField(max_length=70,blank=True)
    observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.nombre


    @classmethod
    def reparticionesRegistradas(self):
        objetos = self.objects.all().order_by('nombre')
        arreglo = []
        for indice,objeto in enumerate(objetos):            
            arreglo.append([])
            arreglo[indice].append(objeto.nombre)
            nombre_reparticion = objeto.nombre 
            arreglo[indice].append("%s" % (nombre_reparticion))
 
        return arreglo   


class Agentes(models.Model):
    #id
    nombre = models.CharField(max_length=60, null=True,unique=True)
    funcion = models.CharField(max_length=60, null=True)
    observacion = models.CharField(max_length=150,blank=True)

    def __str__(self):
        return self.nombre

    @classmethod
    def agentesRegistrados(self):
        objetos = self.objects.all().order_by('nombre')
        arreglo = []
        for indice,objeto in enumerate(objetos):
            print(indice, objeto)           
            arreglo.append([])
            arreglo[indice].append(objeto.nombre)
            nombre_agente = objeto.nombre 
            arreglo[indice].append("%s" % (nombre_agente))
 
        return arreglo   


class Reclamos(models.Model):
    Fecha_reclamo = models.DateField(null=False)
    cod_repart = models.ForeignKey(Reparticion,to_field='nombre', on_delete=models.CASCADE)
    motivo = models.CharField(max_length=100, blank=False)
    Pedido_por = models.CharField(max_length=60, blank=True)
    cod_agente  = models.ForeignKey(Agentes,to_field='nombre', on_delete=models.CASCADE)
    prioridad = [('1','Alta'),('2','Media'),('3','Baja')]
    estado_reclamo = [('1','Realizado'),('2','Pendiente'),('3','Paralizado')]
    prioridad_reclamo = models.CharField(max_length=10,choices=prioridad,blank=True)
    estadia_reclamo = models.CharField(max_length=10,choices=estado_reclamo,blank=True)
    observacion = models.CharField(max_length=150,blank=True) 
    Fecha_realizado = models.DateField(null=True,blank=True)

    
    def clean(self):
        if self.estadia_reclamo == '1' and   self.Fecha_realizado == None:
            raise ValidationError("Si estado del Reclamo es Realizado, Debe ingrear fecha realiazado") 

        if  self.estadia_reclamo == '2' and   self.Fecha_realizado != None:
            raise ValidationError("Si estado del Reclamo es Pendiente, no debe ingrear fecha realiazado") 


class Clientes(models.Model):
    nombre=models.CharField(max_length=30)
    direccion=models.CharField(max_length=50, verbose_name="la Direccion")
    email=models.EmailField(blank=True, null=True)
    tfno=models.CharField(max_length=7)

    def __str__(self):
        return 'el nombre es %s la direccion es %s el email es %s el telefo es %s' % (self.nombre, self.direccion, self.email, self.tfno)



class Articulos(models.Model):
    nombre=models.CharField(max_length=30)
    seccion=models.CharField(max_length=20)
    precio=models.IntegerField()

    def __str__(self):
        return 'el nombre es %s la seccion es %s el precio es %s' % (self.nombre, self.seccion, self.precio)

class Pedidos(models.Model):
    numero=models.IntegerField()
    fecha=models.DateField()
    entregado=models.BooleanField()


# nuevooooo

class Viajero(models.Model):
    apellido = models.CharField(max_length=50)
    nombre = models.CharField(max_length=50)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    dni = models.CharField(max_length=12,blank=True,null=True)
    

class Reserva(models.Model):
    viajero = models.ForeignKey(Viajero, 
                                    on_delete=models.CASCADE,
                                    null=False, blank=False,
                                    related_name='reservo')
    fecha_reserva = models.DateField()
    fecha_llegada = models.DateField(default=timezone.now)
    fecha_salida = models.DateField(default=timezone.now)
    estado_reserva = models.BooleanField(default=False)
    cabana = models.CharField(max_length=50)
    cant_personas = models.IntegerField(blank=True,null=True)

    def __str__(self):
        #return self.viajero
        return 'el Fecha Reserva es %s la cabaña es %s el viajero es %s' % (self.fecha_reserva, self.cabana, self.viajero)
        #return  (self.__apellido)



class Pagos(models.Model):
    viajero = models.ForeignKey(Viajero, 
                                    on_delete=models.CASCADE,
                                    null=False, blank=False,
                                    related_name='pago')
    fecha_pago = models.DateField()
    monto = models.DecimalField(max_digits=10, decimal_places=2)

# -------------- fin de nuevo 


