from rest_framework.permissions import BasePermission

class IsAuthor(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)
    
    def has_object_permission(self, request, view, obj):
        return obj.author == request.user

class IsRater(BasePermission):
    def has_permission(self, request, view):
        return bool(request.user.is_authenticated)

    def has_object_permission(self, request, view, obj):
        return bool(obj.user == request.user)