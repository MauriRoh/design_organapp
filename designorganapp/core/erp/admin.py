from django.contrib import admin
from .models import Category, Estados, Locality, Province, client, Production, Sale, DetSale


# STATES
class ModelAdminEstados(admin.ModelAdmin):
    list_display = (
        'id',
        'state_type',
    )
    # Buscador
    search_fields = ('state_type',)

# Register your models here.
admin.site.register(Estados, ModelAdminEstados)


# CATEGORY
class ModelAdminCategory(admin.ModelAdmin):
    list_display = (
        'name',
        'categorysize',
        'pvp',
        'image',
    )
    search_fields = ('name',)

# Register your models here.
admin.site.register(Category, ModelAdminCategory)


# LOCALITY
class ModelAdminLocality(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    # Buscador
    search_fields = ('name',)

# Register your models here.
admin.site.register(Locality, ModelAdminLocality)


# LOCALITY
class ModelAdminProvince(admin.ModelAdmin):
    list_display = (
        'id',
        'name',
    )
    # Buscador
    search_fields = ('name',)

# Register your models here.
admin.site.register(Province, ModelAdminProvince)


# CLIENTS
class ModeladoVistaCliente(admin.ModelAdmin):
    list_display = (
        'id',
        'surname',
        'name',
        'full_name',
        'mobile',
        'phone',
        'email',
        'province',
        'department',
    )
    #Funciones 
    def full_name(self, obj):
        return obj.surname + ' ' + obj.name
    #Otros filtrados
    search_fields = ('surname', 'name',)
    list_filter = ('department',)
    paginate_by=10

# Register your models here.
admin.site.register(client, ModeladoVistaCliente)


# PRODUCTION
class ModelAdminProduccion(admin.ModelAdmin):
    list_display = (
        'id',
        'cat',
        'name',
        'size',
        'observation',
        'amount',
        'state',
        'product_price',
        'today_date',
        'due_date',
        'image',
    )
    #funciones 
    def full_descriptions(self, obj):
        return obj.cat + ' ' + obj.name + ' ' + obj.size
    # Buscador
    search_fields = ('cat', 'name',)
    # Lista por 
    list_filter = ('state', 'cat', 'size',)

# Register your models here.
admin.site.register(Production, ModelAdminProduccion)


# SALE
class ModelAdminSale(admin.ModelAdmin):
    list_display = (
        'id',
        'cli',
        'date_joined',
        'subtotal',
        'iva',
        'total',
    )

    search_fields = ('date_joined', 'cli',)

# Register your models here.
admin.site.register(Sale, ModelAdminSale)


# SALE DETAIL
class ModelAdminSaleDetail(admin.ModelAdmin):
    list_display = (
        'id',
        'sale',
        'prod',
        'price',
        'cant',
        'subtotal',
    )

    search_fields = ('prod', 'sale',)

# Register your models here.
admin.site.register(DetSale, ModelAdminSaleDetail)
