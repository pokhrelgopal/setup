from rest_framework.permissions import BasePermission, SAFE_METHODS


class CustomPermission(BasePermission):
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(getattr(obj, "can_change")(request))

    def has_permission(self, request, view):
        return True


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True

        return request.user and request.user.is_staff
