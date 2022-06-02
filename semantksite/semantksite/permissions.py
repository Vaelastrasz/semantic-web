from rest_framework import permissions


class CustomUserPermission(permissions.BasePermission):
    message = 'Your editing permissions are not enough for this action!'

    def has_permission(self, request, view):
        if request.method == 'GET':
            return True
        if request.method in ('PUT', 'PATCH') and request.user.role in ('moderator', 'admin'):
            return True
        if request.method in ('POST', 'DELETE') and request.user.role == 'admin':
            return True

        return False