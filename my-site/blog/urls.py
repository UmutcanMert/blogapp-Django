from django.urls import path
from . import views
# http://127.0.0.1:8000/

urlpatterns = [
    path("", views.index,name="home"),
    path("index", views.index),
    path("blogs", views.blogs, name="blogs"),
    path("blogs/<slug:slug>", views.blog_details, name="blog_details"),
    path("category/<slug:slug>",views.blogs_by_category, name = "blogs_by_category")
    
    
]
