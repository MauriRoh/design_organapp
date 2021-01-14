from django.db import models
from django.utils import timezone
from django.db.models import Q, Count
# Imports Módulos
import datetime


# STATES
class EstadosManager(models.Manager):

    def serch_states(self, kword):
        consulta_estados=self.filter(
            Q(state_type__icontains=kword)
        ).order_by('id')
        return consulta_estados


# CATEGORY
class CategoryManager(models.Manager):
    
    def search_category(self, kword):
        consulta=self.filter(
            Q(name__icontains=kword)
        ).order_by('name')

        return consulta


# CATEGORY
class LocalityManager(models.Manager):
    
    def search_locality(self, kword):
        consulta=self.filter(
            Q(name__icontains=kword)
        ).order_by('name')

        return consulta

# PROVINCE
class ProvinceManager(models.Manager):
    
    def search_province(self, kword):
        consulta=self.filter(
            Q(name__icontains=kword)
        ).order_by('name')

        return consulta


# CLIENTS
class ClientsManager(models.Manager):
    
    def search_client(self, kword):
        consulta=self.filter(
            Q(name__icontains=kword) | Q(surname__icontains=kword)
        ).order_by('-id', 'surname', 'name')

        return consulta



# PRODUCTION
class ProductionManager(models.Manager):
    
    def search_production(self, **filters):
        if not filters['date_start']:
            filters['date_start'] = timezone.now().date()

        if not filters['date_end']:
            fecha_futuro=timezone.now().date() + datetime.timedelta(days=300)
            fecha_caducidad = fecha_futuro.strftime("%Y-%m-%d")
            filters['date_end'] = fecha_caducidad

        consulta_production=self.filter(
            due_date__range=(filters['date_start'], filters['date_end'])
        ).filter(
            Q(name__icontains=filters['productionkeyword'])
        )

        return consulta_production.order_by('-id')
       

    def search_id_one(self, kword):
        search_idone=self.filter(
            state__id='1'
        ).filter(
            Q(name__icontains=kword)
        ).order_by('id')

        return search_idone

    def search_id_two(self, kword):
        search_idtwo=self.filter(
            state__id='2'
        ).filter(
            Q(name__icontains=kword)
        ).order_by('id')

        return search_idtwo

    def search_id_three(self, kword):
        search_idthree=self.filter(
            state__id='3'
        ).filter(
            Q(name__icontains=kword)
        ).order_by('id')

        return search_idthree

    def search_id_four(self, kword):
        search_idthree=self.filter(
            state__id='4'
        ).filter(
            Q(name__icontains=kword)
        ).order_by('id')

        return search_idthree


