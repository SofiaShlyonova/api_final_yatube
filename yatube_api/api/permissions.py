from rest_framework import permissions


class IsAuthorOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        return True  # Базовый доступ контролируется IsAuthenticatedOrReadOnly

    def has_object_permission(self, request, view, obj):
        # Разрешаем GET, HEAD, OPTIONS запросы
        if request.method in permissions.SAFE_METHODS:
            return True
        # Разрешаем запись только автору объекта
        return obj.author == request.user
