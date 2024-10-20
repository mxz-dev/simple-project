from django import template
from mag.models import Categories, Posts
from django.utils import timezone
register = template.Library()



@register.inclusion_tag("inc/categories.html")
def get_category():
    posts = Posts.objects.filter(is_published=True, published_date__lt=timezone.now())
    categories = Categories.objects.all()
    cat_dict = {}
    for name in categories:
            cat_dict[name] = posts.filter(category=name).count()
    
    return {'categories':cat_dict}

@register.inclusion_tag("inc/latest_posts.html")
def get_latest_posts():
    posts = Posts.objects.filter(is_published=True,published_date__lt=timezone.now()).order_by("-published_date")[:3]
    return {"last_posts":posts}
@register.inclusion_tag("inc/latest_posts_from_blog.html")
def get_from_posts():
    posts = Posts.objects.filter(is_published=True,published_date__lt=timezone.now()).order_by("-published_date")[:6]
    return {"last_posts":posts}