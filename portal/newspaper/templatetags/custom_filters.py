from django import template

register = template.Library()


@register.filter(name='multiply')
def multiply(value, arg):
    return str(value) * arg


CENSORED = ['Кек', 'Гиббон']


@register.filter(name='censor')
def censor(value):
    text = value.split()
    for word in text:
        if word.lower() in CENSORED:
            value = value.replace(word, '****')
    return value
