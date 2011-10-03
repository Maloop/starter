from django import template
import re
register = template.Library()

@register.simple_tag
def active_url(request, pattern, start=None, end=None):
    """
    First, set the url as a var with {% url customer_detail cc.pk as customer_home %}
    Then do <a class="{% active_url request customer_home 1 1 %}" href=""></a>

    """
    if end:
        pattern = pattern + "$"
    if start:
        pattern = "^" + pattern
    if re.search(pattern, request.path):
        return 'active'
    return ''
