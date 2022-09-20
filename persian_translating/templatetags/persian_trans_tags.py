from django import template

register = template.Library()


@register.filter()
def translate_numbers(value):
    value = str(value)
    eng_to_persian_table = value.maketrans('0123456789', '۰۱۲۳۴۵۶۷۸۹')
    return value.translate(eng_to_persian_table)
