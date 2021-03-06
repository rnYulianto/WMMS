'''
Created on Jun 4, 2017

@author: Asus-PC
'''
from django import template
from django.template.defaultfilters import stringfilter

register = template.Library()

@register.filter
def lookup(d, key):
    return d[key]

@register.filter(is_safe=False)
def get_range(value):    
    return range(value)