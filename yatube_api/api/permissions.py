from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    message = (
        'У вас нет доступных прав на: удаление и редактирование. Зарегистрируйтесь!'
        )

    def has_object_permission(self, request, view, obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.author == request.user
        )
