from rest_framework.permissions import BasePermission


SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS', )


class IsAdminOrReadyOnly(BasePermission):

    """Apenas Usuários is_staff podem fazer operações como POST, PUT E DELETE"""

    def has_permission(self, request, view):
        return bool(request.method in SAFE_METHODS or (request.user and request.user.is_staff))
