from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    '''
    オブジェクトの所有者にのみ編集を許可するカスタム権限
    '''

    def has_object_permission(self, request, view, obj):
        '''
        読み取りアクセス権は許可
        常にGET、HEAD、またはOPTIONSリクエストを許可する
        '''

        if request.method in permissions.SAFE_METHODS:
            return True

        return obj.owner == request.user
