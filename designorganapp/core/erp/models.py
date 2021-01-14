from typing import ItemsView
from django.db import models

# Create your models here.
from datetime import datetime

# Manager
from .managers import EstadosManager, CategoryManager, LocalityManager, ProvinceManager, ClientsManager, ProductionManager
from designorganapp.settings import MEDIA_URL, STATIC_URL

# # Model que permite transfora un objeto en un diccionario
from django.forms import model_to_dict


# STATES
class Estados (models.Model):
    """ Estados producción """ 
    state_type = models.CharField(max_length=20, blank=True, verbose_name='Estado')

    objects = EstadosManager()

    def __str__(self):
        return self.state_type
    
    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'states'
        ordering = ['id']


# CATEGORY
class Category(models.Model):
    """ Tipo de Indumentarias """
    name = models.CharField(max_length=150, unique=True, verbose_name='Tipo de Prenda')
    categorysize = models.CharField(max_length=4, blank=True, default='', verbose_name='Telle')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    image = models.ImageField(upload_to='category/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    
    objects = CategoryManager()

    def __str__(self):
        return self.name

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.name.toJSON()
        # item['categorysize'] = self.categorysize.toJSON()
        # item['pvp'] = format(self.pvp, '.2f')
        # item['image'] = self.get_image()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'image/empty.png')

    class Meta:
        verbose_name = 'Tipo de Prenda'
        verbose_name_plural = 'Tipo de Prendas'
        db_table = 'category'
        ordering = ['name']


# LOCALITY
class Locality(models.Model):
    """ Departamento / Partido """
    name = models.CharField(max_length=50, unique=True, verbose_name='Departamento / Partido')

    objects = LocalityManager()

    def __str__(self):
        return self.name

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Localidad'
        verbose_name_plural = 'Localidades'
        db_table = 'locality'
        ordering = ['name']


# PROVINCE
class Province(models.Model):
    """ Provincia """
    name = models.CharField(max_length=30, unique=True, verbose_name='Provincia')

    objects = ProvinceManager()

    def __str__(self):
        return self.name

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        return item

    class Meta:
        verbose_name = 'Provincia'
        verbose_name_plural = 'Provincias'
        db_table = 'province'
        ordering = ['name']


# Clients
class client(models.Model):
    GENDER = (
        ('M','MASCULINO'),
        ('F','FEMENINO'),
        ('O','OTRO'),
    )
    name = models.CharField(max_length=30, null=False, blank=False, verbose_name='Nombre')
    surname = models.CharField(max_length=30, null=False, blank=False, verbose_name='Apellido')
    gender = models.CharField(max_length=1, choices=GENDER, default='O', verbose_name='Género')
    mobile = models.CharField(max_length=20, blank=True, default='0', verbose_name='Móbil')
    phone = models.CharField(max_length=20, blank=True, default='0', verbose_name='Teléfono')
    email = models.EmailField(blank=True, default='', verbose_name='Email')
    address = models.CharField(max_length=30, blank=True, default='', verbose_name='Dirección')
    department = models.ForeignKey(Locality, on_delete=models.CASCADE, verbose_name='Departamento')
    neighborhood = models.CharField(max_length=20, blank=True, default='', verbose_name='Barrio')
    localities = models.CharField(max_length=20, blank=True, default='', verbose_name='Localidad')
    province = models.ForeignKey(Province, on_delete=models.CASCADE, verbose_name='Provincia')
    postal_code = models.CharField(max_length=8, blank=True, default='', verbose_name='Código Postal')
    others = models.TextField(blank=True, default='', verbose_name='Otros')
    
    objects = ClientsManager()

    def __str__(self):
        return self.surname

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        item['name'] = self.name.toJSON()
        item['surname'] = self.surname.toJSON()
        item['gender'] = {'id': self.gender, 'name': self.get_gender_display()}
        item['mobile'] = self.mobile.toJSON()
        item['phone'] = self.phone.toJSON()
        item['email'] = self.email.toJSON()
        item['address'] = self.address.toJSON()

        item['department'] = self.department.toJSON()

        item['neighborhood'] = self.neighborhood.toJSON()

        item['localities'] = self.localities.toJSON()

        item['province'] = self.province.toJSON()

        item['postal_code'] = self.postal_code.toJSON()
        item['others'] = self.others.toJSON()
        item['full_name'] = self.get_full_name()
        return item

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'
        db_table = 'clients'
        ordering = ['surname']
        unique_together = ('surname', 'name', 'email')


# PRODUCTION
class Production(models.Model):
    """ Producción y sus Estados """
    name = models.CharField(max_length=70, blank=True, default='', verbose_name='Descripción')
    cat = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name='Tipo prenda')
    size = models.CharField(max_length=4, blank=True, default='', verbose_name='Telle')
    observation = models.TextField(blank=True, default='', verbose_name='Observaciones')
    amount = models.PositiveIntegerField(default=1, verbose_name='Cantidad')
    state = models.ForeignKey(Estados, on_delete=models.CASCADE, verbose_name='Estado Producción')
    product_price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio producto')
    today_date = models.DateField(default=datetime.now, verbose_name='Creación')
    due_date = models.DateField(default=datetime.now, verbose_name='Vencimiento')
    image = models.ImageField(upload_to='produccion/%Y/%m/%d', null=True, blank=True, verbose_name = 'Imagen')
   
    objects = ProductionManager()

    def __str__(self):
        return self.name
    
    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    # ver vídeo 77 para ver como convertir las fecha e imágenes para poder ser enviado en forma correcta y no arroje errores
    def toJSON(self):
        item = model_to_dict(self)
        item['cat'] = self.cat.toJSON()
        item['name'] = self.name.toJSON()
        item['size'] = self.size.toJSON()
        item['observation'] = self.observation.toJSON()
        item['amount'] = self.amount.toJSON()
        item['state'] = self.state.toJSON()
        item['product_price'] = format(self.product_price, '.2f')
        item['today_date'] = self.today_date.strftime('%Y-%m-%d')
        item['due_date'] = self.due_date.strftime('%Y-%m-%d')
        item['image'] = self.get_image()
        item['full_name'] = self.get_full_name()
        return item
    
    # Función para cargar imagen por defecto en caso de que este vacio o no se haya cargado ninguna
    # caso contrario, se carga la imagen seleccionada 
    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'image/empty.png')
        
    class Meta:
        verbose_name = 'Producción'
        verbose_name_plural = 'Producciones'
        db_table = 'production'
        ordering = ['-id']

# SALE
class Sale(models.Model):
    """ Ventas """
    cli = models.ForeignKey(client, on_delete=models.CASCADE, verbose_name='Cliente venta')
    date_joined = models.DateField(default=datetime.now, verbose_name='Fecha venta')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    iva = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    total = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
    
    def __str__(self):
        return self.cli.surname

    # El método "model_to_dict" me permite obtener un diccionario a partir del modelo que nostros le enviamos
    def toJSON(self):
        item = model_to_dict(self)
        item['cli'] = self.cli.toJSON()
        item['date_joined'] = self.date_joined.strftime('%Y-%m-%d')
        item['subtotal'] = format(self.subtotal, '.2f')
        item['iva'] = format(self.iva, '.2f')
        item['total'] = format(self.total, '.2f')
        item['det'] = [i.toJSON() for i in self.detsale_set.all()]
        return item
        
    class Meta:
        verbose_name = 'Venta'
        verbose_name_plural = 'Ventas'
        db_table = 'sale'
        ordering = ['id']
    

# DETAIL OF SALE
class DetSale(models.Model):
    """ Detalle de las Ventas """
    sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name='Venta')
    prod = models.ForeignKey(Production, on_delete=models.CASCADE, verbose_name='Producción')
    price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio producto')
    cant = models.IntegerField(default=0, verbose_name='Cantidad')
    subtotal = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)

    def __str__(self):
        return self.prod.name

    class Meta:
        verbose_name = 'Detalle de Venta'
        verbose_name_plural = 'Detalle de Ventas'
        db_table = 'sale_detail'
        ordering = ['id']


