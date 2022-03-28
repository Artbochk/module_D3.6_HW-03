from django import template

register = template.Library()

CENSOR_WORDS = {
    'Редиска':'Р******',
    'Редиска!':'Р******!',
    'редиска':'р******',
}

@register.filter()
def censor(value):
    list_ = list(value.split())
    for v in list_:
        if v in CENSOR_WORDS.keys():
            value = value.replace(v, CENSOR_WORDS[v])
    return value
