from django.template.defaulttags import register


@register.filter
def my_float(value):
    # value =
    return f"{value:.1f}"
