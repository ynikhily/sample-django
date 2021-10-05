from django import template

register = template.Lirary()

@register.filter(name='cut_it')
def cut_it(value, arg):
    """
    Cuts out all value of arg from string
    """

    return value.replace(arg,'')

# register.filter('cut_it', cut_its)
