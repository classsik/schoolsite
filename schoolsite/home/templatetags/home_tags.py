from django import template
from home.models import *
from blog.models import *

register = template.Library()


@register.inclusion_tag(
    'home/tags/blog_listing_homepage.html',
    takes_context=True
)
def blog_listing_homepage(context, count=5):  #count=3 выводит 3 последних поста
    blogs = BlogPage.objects.live().order_by('-date')  #фильтр по дате от последнего поста
    return {
        'blogs': blogs[:count],
        'request': context['request'],
    }