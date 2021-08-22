from rest_framework.permissions import BasePermission, SAFE_METHODS


# SAFE_METHOD => 'GET', 'HEAD', 'OPTIONS'

# write a permission only for super user
class IsSuperUser(BasePermission):
    """
    Allows access only to super users.
    """

    def has_permission(self, request, view):
        return bool(request.user.is_superuser and request.user)


class IsStaffOrReadOnly(BasePermission):
    """
        The request is staff as a user, or is a read-only request.
    """

    def has_permission(self, request, view):
        return bool(
            request.user.is_staff and
            request.user or
            request.method in SAFE_METHODS
        )

