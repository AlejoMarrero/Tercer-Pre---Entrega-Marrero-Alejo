from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import *
from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView
from django.http import HttpResponseBadRequest


def pagina_principal(request):
    return render(request, "aplicacion/index.html")

#Sección Productos:
class ProductoList(ListView):
    model = Producto

class ProductoCreate(CreateView):
    model = Producto
    fields = ["modelo","descripcion","stock","precio"]
    success_url = reverse_lazy("productos")

class ProductoUpdate(UpdateView):
    model = Producto
    fields = ["modelo","descripcion","stock","precio"]
    success_url = reverse_lazy("productos")

class ProductoDelete(DeleteView):
    model = Producto
    success_url = reverse_lazy("productos")


#Sección Proveedores:
class ProveedorList(ListView):
    model = Proveedor

class ProveedorCreate(CreateView):
    model = Proveedor
    fields = ["razon_social", "cuit", "producto", "cantidad", "monto_total"]
    success_url = reverse_lazy("proveedores")

class ProveedorUpdate(UpdateView):
    model = Proveedor
    fields = ["razon_social", "cuit", "producto", "cantidad", "monto_total"]
    success_url = reverse_lazy("proveedores")

class ProveedorDelete(DeleteView):
    model = Proveedor
    success_url = reverse_lazy("proveedores")



#Sección Ventas:
class VentaList(ListView):
    model = Venta

class VentaCreate(CreateView):
    model = Venta
    fields = ["cliente", "documento", "modelo", "precio_venta"]
    success_url = reverse_lazy("ventas")

class VentaUpdate(UpdateView):
    model = Venta
    fields = ["cliente", "documento", "modelo", "precio_venta"]
    success_url = reverse_lazy("ventas")

class VentaDelete(DeleteView):
    model = Venta
    success_url = reverse_lazy("ventas")


#Seccion busqueda:

def buscar(request):
    if request.method == "POST":
        if 'buscando' in request.POST:
            buscando = request.POST['buscando']
            productos = Producto.objects.filter(modelo__contains = buscando)
            proveedores = Proveedor.objects.filter(razon_social__contains = buscando)
            venta = Venta.objects.filter(id__contains = buscando)
            return render(request, 
            'aplicacion/buscar.html', 
            {'buscando': buscando,
            'productos': productos,
            'proveedores': proveedores,
            'ventas': venta,})
        else:
            # Return a bad request response if 'buscando' key is missing
            return HttpResponseBadRequest('El parámetro "buscando" no se encontró en la solicitud POST.')
    else:
        return render(request, 'aplicacion/buscar.html', {})

    

