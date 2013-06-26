from django import template
import jsconstants

register = template.Library()

@register.inclusion_tag('helpers/jsconstants/constants.html', name="jsconstants")
def jsconstants_():
    return { 
        'constants' : jsconstants.get_constants_json() 
    }
