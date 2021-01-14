# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView
from core.erp.forms import RegisterStatesUpDateForm
from core.erp.models import Estados
from core.erp.forms import RegisterStatesUpDateForm 
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
################## ESTADOS ##################
# Lista los Estados
class EstadosListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Estados
    template_name = 'states/list.html'
    context_object_name ='liststates'
    permission_required = 'view_category'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Lista de Estados'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        return context

    def get_queryset(self):
        keyword_estados = self.request.GET.get("estadokeyword",'')
        queryset = Estados.objects.serch_states(keyword_estados)
        return queryset



# class EstadosCreate(CreateView):
#     model = Estados
#     form_class = RegisterStatesUpDateForm 
#     template_name = 'states/create.html'
#     url_redirect = success_url
#     success_url = reverse_lazy('productos_app:listar-estados')

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Crear Estado'
#         context['nav_clients'] = 'Cliente'
#         context['nav_productions'] = 'Producción'
#         context['nav_sale'] = 'Ventas'
#         context['action'] = 'add'
#         context['list_url'] = self.success_url
#         return context


# class EstadosUpdate(UpdateView):
#     model = Estados
#     form_class = RegisterStatesUpDateForm 
#     template_name = 'states/update.html'
#     url_redirect = success_url
#     success_url = reverse_lazy('productos_app:category-list')


#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['title'] = 'Editar Estado'
#         context['nav_clients'] = 'Cliente'
#         context['nav_productions'] = 'Producción'
#         context['nav_sale'] = 'Ventas'
#         context['action'] = 'edit'
#         context['list_url'] = self.success_url
#         return context