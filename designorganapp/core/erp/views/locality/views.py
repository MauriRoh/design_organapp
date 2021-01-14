# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from core.erp.forms import LocalityForm
from core.erp.models import Locality
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render, redirect



class LocalityList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Locality
    template_name = 'locality/list.html'
    context_object_name ='listlocality'
    permission_required = 'view_category'

    # Métod Decorador y Dispatch. El Dispach está deshabilitado xq sino la vista queda desprotegida, sin el CSRF
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    # # def post(self, request, *args, **kwargs):
    # #     data={}
    # #     try:
    # #         action = request.POST['action']
    # #         if action == 'searchdatacategory':
    # #             data = []
    # #             for i in Category.objects.all():
    # #                 data.append(i.toJSON())
    # #         else:
    # #             data['error'] = 'Ha ocurrido un error'
    # #     except Exception as e:
    # #         data ['error'] = str(e)
    # #     return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Localidades'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        return context

    #Busca el Tipo de Productos
    def get_queryset(self):
        key_word_list = self.request.GET.get("localitykeyword", '')
        queryset = Locality.objects.search_locality(key_word_list)
        return queryset



class LocalityCreate(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Locality
    form_class = LocalityForm
    template_name = 'locality/create.html'
    success_url = reverse_lazy('productos_app:locality-list')
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
        context['title'] = 'Nueva Localidad'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'add'
        context['list_url'] = self.success_url
        return context



class LocalityUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Locality
    form_class = LocalityForm
    template_name = 'locality/create.html'
    success_url = reverse_lazy('productos_app:locality-list')
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
        context['title'] = 'Editar Registro de Localidad'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context
