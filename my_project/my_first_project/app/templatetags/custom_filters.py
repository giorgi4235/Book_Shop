from django import template

register = template.Library()

@register.filter
def star_rating(value):
    """Convert a numerical rating into a star rating."""
    stars = '★' * value
    return stars
