from django.http import Http404


class SuperuserAccessMixin():
    def dispatch(self, request, *args, **kwargs):
        if request.user.is_superuser:
            return super().dispatch(request, *args, **kwargs)
        else:
            return Http404('شما به این صفحه دسترسی ندارید')
