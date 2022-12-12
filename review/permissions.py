from rest_framework.permissions import BasePermission, SAFE_METHODS

class isAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
            
        if request.user.is_authenticated:
            return True
            
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            #если просто чтение
            return True
        if not request.user.is_authenticated:
            #если юзера нет
            return False
        if request.user == obj.author:
            #если пользователь - автор комментария (рейтинга)
            return True
            