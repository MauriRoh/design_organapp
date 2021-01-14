# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from core.erp.forms import RegisterClientsAddForm
from core.erp.models import client
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# LISTAR CLIENTS
class ClientsList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = client
    template_name = 'client/list.html'
    context_object_name ='listacliente'
    permission_required = 'view_category'

    # Métod Decorador y Dispatch. El Dispach está deshabilitado xq sino la vista queda desprotegida, sin el CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # def post(self, request, *args, **kwargs):
    #     data={}
    #     try:
    #         action = request.POST['action']
    #         if action == 'searchdataclient':
    #             data = []
    #             for i in Clientes.objects.all():
    #                 data.append(i.toJSON())
    #         else:
    #             data['error'] = 'Ha ocurrido un error'
    #     except Exception as e:
    #         data ['error'] = str(e)
    #     return JsonResponse(data, safe=False)

    #Busca el cliente
    def get_queryset(self):
        key_word_list = self.request.GET.get("clientkeyword", '')
        queryset = client.objects.search_client(key_word_list)
        return queryset
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Clientes'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        return context


# REGISTRAR O CREAR UN NUEVO CLIENTE
class ClientsCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = client
    form_class = RegisterClientsAddForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('productos_app:lista-clientes')
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
        context['title'] = 'Nuevo Cliente'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context
  

# MODIFICAR UN REGISTRO DE CLIENTE
class ClientsUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = client
    form_class = RegisterClientsAddForm
    template_name = 'client/create.html'
    success_url = reverse_lazy('productos_app:lista-clientes')
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
        context['title'] = 'Editar Registro del Cliente'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


# ELIMINAR UN CLIENTE
class ClientsDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = client
    template_name = 'client/delete.html'
    success_url = reverse_lazy('productos_app:lista-clientes')
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
        context['title'] = 'Eliminar Registro de un Cliente'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['list_url'] = self.success_url
        return context
