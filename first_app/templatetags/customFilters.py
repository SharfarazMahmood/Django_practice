from django import template

register = template.Library()

def customFilters(value, arg):
    return value + ' ##added part from custom filter##' + arg

register.filter('custom_filter', customFilters)
