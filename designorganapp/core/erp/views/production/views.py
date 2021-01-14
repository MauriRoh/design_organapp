# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.erp.forms import RegisterProductionAddForm
from core.erp.models import Production
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt



#Lista las producciones
class ProductionList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Production
    template_name = 'production/list.html'
    context_object_name ='listproductions'
    permission_required = 'view_category'

    # # Métod Decorador y Dispatch. El Dispach está deshabilitado xq sino la vista queda desprotegida, sin el CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def post(self, request, *args, **kwargs):
        data={}
        try:
            action = request.POST['action']
            if action == 'searchdataproduction':
                data = []
                for i in Production.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data ['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Producciones'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        return context

    def get_queryset(self):
        queryset = Production.objects.search_production(
            productionkeyword=self.request.GET.get("productionkeyword", ''),
            date_start=self.request.GET.get("date_start", ''),
            date_end=self.request.GET.get("date_end", ''),
        )
        return queryset


# Crear una Producción de un producto
class ProductionCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Production
    form_class = RegisterProductionAddForm
    template_name = 'production/create.html'
    success_url = reverse_lazy('productos_app:listar-produccion')
    permission_required = 'add_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Nueva Producción'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context


# Modificar dato/s de un registro
class ProductionUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Production
    form_class = RegisterProductionAddForm
    template_name = 'production/create.html'
    success_url = reverse_lazy('productos_app:listar-produccion')
    permission_required = 'change_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
  
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Editar Registro de Producción'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


# Eliminar un registro de la BD
class ProductionDelete(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Production
    template_name = 'production/delete.html'
    success_url = reverse_lazy('productos_app:listar-produccion')
    permission_required = 'delete_category'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminar Registro de un Producción'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['list_url'] = self.success_url
        return context


# Detallar la tarea de cada producción
class ProductionDetail(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Production
    template_name = 'production/detail.html'
    permission_required = 'view_category'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
