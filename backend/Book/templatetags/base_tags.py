from django import template

# from django.contrib.contenttypes.models import ContentType


register = template.Library()


@register.inclusion_tag("registration/partial/link.html")
def link(request, link_name, content, classes):
    return {
        'request': request,
        'link_name': link_name,
        'link': f'account:{link_name}',
        'content': content,
        'classes': classes,
    }
