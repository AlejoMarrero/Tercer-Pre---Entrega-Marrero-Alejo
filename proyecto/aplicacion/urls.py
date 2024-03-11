from django.urls import path,include
from .views import *
urlpatterns = [
    path('', pagina_principal, name='home'), #pagina_principal va a ser una funcion.

#_______________Productos
    path('productos/',ProductoList.as_view(),name="productos"),
    path('productos_create/',ProductoCreate.as_view(),name="productos_create"),
    path('productos_update/<int:pk>/',ProductoUpdate.as_view(),name="productos_update"),
    path('productos_delete/<int:pk>/',ProductoDelete.as_view(),name="productos_delete"),


#_______________Proveedores
    path('proveedores/',ProveedorList.as_view(),name="proveedores"),
    path('proveedores_create/',ProveedorCreate.as_view(),name="proveedores_create"),
    path('proveedores_update/<int:pk>/',ProveedorUpdate.as_view(),name="proveedores_update"),
    path('proveedores_delete/<int:pk>/',ProveedorDelete.as_view(),name="proveedores_delete"),


#_______________Ventas
    path('ventas/',VentaList.as_view(),name="ventas"),
    path('ventas_create/',VentaCreate.as_view(),name="ventas_create"),
    path('ventas_update/<int:pk>/',VentaUpdate.as_view(),name="ventas_update"),
    path('ventas_delete/<int:pk>/',VentaDelete.as_view(),name="ventas_delete"),


#______________Busqueda
    path('buscar/',buscar,name="buscar"),

]
