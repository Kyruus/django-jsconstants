from django import template
from django_jsconstants import jsconstants

register = template.Library()

@register.inclusion_tag('constants.html', name="jsconstants")
def jsconstants_(*modules):
    return { 
        'constants' : jsconstants.get_constants_json(*modules) 
    }
