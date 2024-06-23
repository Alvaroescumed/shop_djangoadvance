from rest_framework import permissions

# Creamos un permiso que permite a cualquier persona sin autentificacion a ver los productos disponibles y el catalogo

class isClient(permissions.BasePermission):

    def has_permission(self, request, view):

        if request.method in permissions.SAFE_METHODS:
            return True
        
        return request.user.is_authenticated and request.user.groups.filter(name='Gerentes').exists()

# Creamos otro permiso que solo permita leer a usuarios autenticados pero que el resto de metodos solo lo pueden ejecutar gerentes   
class isGerente(permissions.BasePermission):

    def has_permission(self, request, view):
       
       if request.method in permissions.SAFE_METHODS:
           return request.user.is_authenticated
       
       return request.user.is_authenticated and request.user.groups.filter(name='Gerentes').exists()