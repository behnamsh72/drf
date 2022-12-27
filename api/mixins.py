from cfehome.permissions import IsStaffEditorPermission
from rest_framework import permissions
class StaffEditorPermissionMixin():
    permission_classes=[permissions.IsAdminUser,IsStaffEditorPermission]


class UserQuerySetMixin():
    user_field='user'
    def get_queryset(self,*args,**kwargs):
        user=self.request.user
        allow_staff_view=False
        lookup_data={}
        lookup_data[self.user_field]=user
        print(lookup_data)
        qs=super().get_queryset(*args,**kwargs)
        print(qs)
        #show all products data to is_staff users only
        if self.allow_staff_view and user.is_staff:
            return qs
        #show all products data to admin user
        # if user.is_admin:
        #     return qs
        return qs.filter(**lookup_data)


