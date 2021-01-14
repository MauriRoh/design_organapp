# MIXIN
from django.contrib.auth.mixins import LoginRequiredMixin
from core.erp.mixins import IsSuperuserMixin, ValidatePermissionRequiredMixin
#
from django.http import JsonResponse
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DetailView
from core.erp.forms import EditDesignImpressionMakingSublimationsForm
from core.erp.models import Production
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt


################## PRODUCCIÓN SUBLIMACION (ID THREE) ##################
class ProductionIdThreeList(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    template_name = 'sublimation/list.html'
    context_object_name ='listidthreeproductions'
    permission_required = 'view_category'
    
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Estado - Sublimación'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        return context

    def get_queryset(self):
        keyword_id = self.request.GET.get("keyword_id_three",'')
        queryset = Production.objects.search_id_three(keyword_id)

        return queryset



class ProductionIdThreeUpdate(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Production
    form_class = EditDesignImpressionMakingSublimationsForm
    template_name = 'sublimation/update.html'
    success_url = reverse_lazy('productos_app:listar-id-three-produccion')
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
        context['title'] = 'Editar Estado - Sublimación'
        context['nav_clients'] = 'Cliente'
        context['nav_productions'] = 'Producción'
        context['nav_sale'] = 'Ventas'
        context['action'] = 'edit'
        context['list_url'] = self.success_url
        return context


# Detallar la tarea de cada producción
class ProductionIdThreeDetail(LoginRequiredMixin, ValidatePermissionRequiredMixin, DetailView):
    model = Production
    template_name = 'sublimation/detail.html'
    permission_required = 'view_category'

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
