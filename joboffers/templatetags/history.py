from django import template

from ..models import JobOffer


register = template.Library()


@register.filter
def verbose_name(field_item):
    field_name, _ = field_item
    meta = JobOffer.get_options()  # Poner público desde joboffer
    field = meta.get_field(field_name)
    return field.verbose_name


@register.filter
def value(field_item):
    field_name, field_value = field_item
    meta = JobOffer.get_options()  # Poner público desde joboffer
    field = meta.get_field(field_name)

    attr_name = field.attname  # Foreign keys use a different attribute name
    joboffer = JobOffer(**{attr_name: field_value})

    display_function = getattr(joboffer, f"get_{field_name}_display", None)

    if display_function:
        return display_function()
    else:
        return getattr(joboffer, field_name)
