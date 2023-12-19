from rest_framework.permissions import BasePermission


class IsAdmin(BasePermission):

    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.role == 'admin':
            return True
        return False


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            if request.user == obj.author or request.user.role == 'admin':
                return True
            return False
