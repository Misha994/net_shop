from django import template

register = template.Library()

@register.filter
def sort(users):
    return sorted([str(i) for i in sorted(users.employee.all())])





