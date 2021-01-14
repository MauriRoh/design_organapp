import json
import os

# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.erp.forms import SaleForm, SaleProductionStockForm
from core.erp.models import Category, client, Production, Sale, DetSale
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



# from django.conf import settings
# from django.db import transaction
# from django.db.models import Q
# from django.http import HttpResponse
# from django.template.loader import get_template
# from xhtml2pdf import pisa


# CREATE SALE
class SaleCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Sale
    second_model = Category
    form_class = SaleForm
    template_name = 'sale/create.html'
    success_url = reverse_lazy('productos_app:sale-create')
    permission_required = 'add_sale'
    url_redirect = success_url

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'search_products':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

  

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Venta'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        context['entity'] = 'Ventas'
        context['formStock'] = SaleProductionStockForm()
        return context