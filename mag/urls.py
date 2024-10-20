from django.urls import path
from .views import *
app_name = 'mag'
urlpatterns = [
    path("", home_view, name="home_view"),
    path("about", about_view, name="about_view"),
    path("contact", contact_view, name="contact_view"),
    path("blog", blog_view, name="blog_view"),
    path("post/<int:pk>", post_view, name="post_view"),
    path("blog/category/<str:category>", blog_view, name="filter_by_category_view")
]
