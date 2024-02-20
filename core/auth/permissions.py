from rest_framework.permissions import BasePermission

class AdminOnlyPermission(BasePermission):

    def has_permission(self, request, view):
        if request.user.user_type == 2:
            return True
        
        return False