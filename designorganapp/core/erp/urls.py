from django.urls import path
from core.erp.views.states.views import EstadosListView
from core.erp.views.category.views import CategoryList, CategoryCreate, CategoryUpdate
from core.erp.views.locality.views import LocalityList, LocalityCreate, LocalityUpdate
from core.erp.views.province.views import ProvinceList, ProvinceCreate, ProvinceUpdate
from core.erp.views.client.views import ClientsList, ClientsCreate, ClientsUpdate, ClientsDeleteView
from core.erp.views.design.views import ProductionIdOneList, ProductionIdOneUpdate, ProductionIdOneDetail
from core.erp.views.impression.views import ProductionIdTowList, ProductionIdTwoUpdate, ProductionIdTwoDetail
from core.erp.views.production.views import ProductionCreate, ProductionList, ProductionUpdate, ProductionDelete, ProductionDetail
from core.erp.views.sublimation.views import ProductionIdThreeList, ProductionIdThreeUpdate, ProductionIdThreeDetail
from core.erp.views.making.views import ProductionIdFourList, ProductionIdFourUpdate, ProductionIdFourDetail
from core.erp.views.dashboard.views import DashboardView
from core.erp.views.sale.views import SaleCreateView


app_name = 'productos_app'

urlpatterns = [
        
     # STATES
    path('states/list/', EstadosListView.as_view(), name='listar-estados'),
    # path('states/create/', EstadosCreate.as_view(), name='alta-estados'),
    # path('states/update/<int:pk>/', EstadosCreate.as_view(), name='modificar-estados'),

    # CATEGORY/ TIPO DE PRENDAS
    path('category/list/', CategoryList.as_view(), name='category-list'),
    path('category/add/', CategoryCreate.as_view(), name='category-create'),
    path('category/update/<int:pk>/', CategoryUpdate.as_view(), name='category-update'),
    #path('category/delete/<int:pk>/', CategoryDelete.as_view(), name='category-delete'),

    # LOCALITY
    path('locality/list/', LocalityList.as_view(), name='locality-list'),
    path('locality/create/', LocalityCreate.as_view(), name='locality-create'),
    path('locality/update/<int:pk>/', LocalityUpdate.as_view(), name='locality-update'),

    # PROVINCE
    path('province/list/', ProvinceList.as_view(), name='province-list'),
    path('province/create/', ProvinceCreate.as_view(), name='province-create'),
    path('province/update/<int:pk>/', ProvinceUpdate.as_view(), name='province-update'),
    
    # CLIENT
    path('client/list/', ClientsList.as_view(), name='lista-clientes'),
    path('client/create/', ClientsCreate.as_view(), name='alta-cliente'),
    path('client/update/<int:pk>/', ClientsUpdate.as_view(), name='modificar-clientes'),
    path('client/delete/<int:pk>/', ClientsDeleteView.as_view(), name='eliminar-clientes'), 

     # DESIGN
    path('design/list/', ProductionIdOneList.as_view(), name='listar-id-one-produccion'),
    path('design/update/<pk>/', ProductionIdOneUpdate.as_view(), name='modificar-id-one-produccion'),
    path('design/detail/<pk>/', ProductionIdOneDetail.as_view(), name='detallar-id-one-produccion'),

    # IMPRESSION
    path('impression/list/', ProductionIdTowList.as_view(), name='listar-id-two-produccion'),
    path('impression/update/<pk>/', ProductionIdTwoUpdate.as_view(), name='modificar-id-two-produccion'),
    path('impression/detail/<pk>/', ProductionIdTwoDetail.as_view(), name='detallar-id-two-produccion'),

    # MAKING (Confección)
    path('making/list/', ProductionIdFourList.as_view(), name='listar-id-four-produccion'),
    path('making/update/<pk>/', ProductionIdFourUpdate.as_view(), name='modificar-id-four-produccion'),
    path('making/detail/<pk>/', ProductionIdFourDetail.as_view(), name='detallar-id-four-produccion'),

    # PRODUCTION       
    path('production/create/', ProductionCreate.as_view(), name='alta-produccion'),
    path('production/list/', ProductionList.as_view(), name='listar-produccion'),
    path('production/update/<pk>/', ProductionUpdate.as_view(), name='modificar-produccion'),
    path('production/delete/<pk>/', ProductionDelete.as_view(), name='eliminar-produccion'),
    path('production/detail/<pk>/', ProductionDetail.as_view(), name='detallar-produccion'),

    # SUBLIMATION
    path('sublimation/list/', ProductionIdThreeList.as_view(), name='listar-id-three-produccion'),
    path('sublimation/update/<pk>/', ProductionIdThreeUpdate.as_view(), name='modificar-id-three-produccion'),
    path('sublimation/detail/<pk>/', ProductionIdThreeDetail.as_view(), name='detallar-id-three-produccion'),

    # PANEL DASHBOARD
    path('dashboard/', DashboardView.as_view(), name='dashboard'),
    
    # SALE
    path('sale/create/', SaleCreateView.as_view(), name='sale-create'),
    
]