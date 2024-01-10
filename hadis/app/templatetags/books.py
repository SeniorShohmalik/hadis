from django import template
from django.template.defaultfilters import stringfilter
from django.utils.safestring import mark_safe

register = template.Library()

from re import IGNORECASE, compile, escape as rescape

register = template.Library()

@register.filter(name='highlight')
def highlight(text, search):
    rgx = compile(rescape(search), IGNORECASE)
    return mark_safe(
        rgx.sub(
            lambda m: '<b class="text text-danger">{}</b>'.format(m.group()),
            text
        )
    )
