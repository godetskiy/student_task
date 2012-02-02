#-*-coding: utf-8 -*-
from django import template
from django.core import urlresolvers
from django.contrib.contenttypes.models import ContentType

register = template.Library()

class EditListNode(template.Node):
    def __init__(self, value):
        self.var = template.Variable(value)

    def render(self, context):
        var = self.var.resolve(context)
        ctype = ContentType.objects.get_for_model(type(var))
        link = u'admin:%s_%s_change' % (ctype.app_label, ctype.model)
        return urlresolvers.reverse(link, args=(var.id,))

@register.tag
def edit_list(parser, token):
    try:
        tag_name, value = token.split_contents()
    except ValueError:
        msg = 'Тег %r требует один аргумент' % token.split_contents()[0]
        raise template.TemplateSyntaxError(msg)
    return EditListNode(value)

