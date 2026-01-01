from rest_framework.permissions import SAFE_METHODS, BasePermission


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.method == 'DELETE':
            return request.user.role == 'admin'
        return request.user and request.user.role in ['manager', 'support', 'admin']
    
    
class productPermission(BasePermission):

    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user.is_authenticated

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        
        user = request.user

        if user.is_staff:
            if request.method == "DELETE":
                return obj.owner == user
            return True
        return obj.owner == user