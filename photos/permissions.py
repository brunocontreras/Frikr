# -*- coding: utf-8 -*-
from rest_framework.permissions import BasePermission


class UserPermission(BasePermission):

    # Aquí entra siempre.
    def has_permission(self, request, view):
        """
        Sólo los usuarios no autenticados puede crear un usuario
        Sólo los admin pueden ver el listado de usuarios.
        Un usuario sólo puede ver su perfil, salvo que sea admin que ve todos.
        Un usuario sólo puede actualizar su perfil, salvo que sea admin que puede actualizar todos
        Un usuario sólo puede borrar su perfil, salvo que sea admin que puede borrar todos
        """

        # Importamos dinámicamente UserDetailAPI. Sólo en el momento que se ejecuta el método se carga el módulo.
        # Si lo importamos arriba generaría una dependencia cíclica.
        if view.action and view.action.lower() == "list" and not request.user.is_authenticated():
            return True
        elif request.user.is_superuser:
            return True
        elif view.action.lower() in ['retrieve', 'update', 'destroy']:
            return True
        return False


    # Aquí entra si la vista es de detalle.
    # Tanto has_permission como has_object_permission tienen que devolver True.
    def has_object_permission(self, request, view, obj):
        return obj == request.user or request.user.is_superuser