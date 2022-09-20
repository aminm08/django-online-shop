from django import template

register = template.Library()


@register.filter()
def active_comments(comments):
    return [comment for comment in comments if comment.active]
