from django.shortcuts import render
from django.http.response import HttpResponse
from blog.models import Blog, Category


data = {
    "blogs":[ 
        {   "id":1,
            "title": "Github Page",
            "image": "github.png",
            "is_active": True,
            "is_home": False,
            "description": "My github public repo",
            "link_explain":"Github sayfama ulaşmak için tıklayınız",
            "link":'https://github.com/UmutcanMert',
        },
        {
            "id":2,
            "title": "Python Course",
            "image": "python.png",
            "is_active": False,
            "is_home": True,
            "description": "it was very good course",
            "link_explain":"Kurs sayfasına ulaşmak için tıklayınız",
            "link":'https://www.udemy.com/course/python-dersleri/',
        },
        {
            "id":3,
            "title": "Django Course",
            "image": "django.png",
            "is_active": True,
            "is_home": True,
            "description": "it is very good course",
            "link_explain":"Kurs sayfasına ulaşmak için tıklayınız",
            "link":'https://www.udemy.com/course/python-dersleri/',
        }
    ]
}


# Create your views here.
def index(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
        
    }
    return render(request,"blog/index.html",context)

def blogs(request):
    context = {
        "blogs": Blog.objects.all(),
        "categories": Category.objects.all()
        
    }
    return render(request,"blog/blogs.html",context)

def blog_details(request, slug):
    blog = Blog.objects.get(slug=slug)
    
    return render(request,"blog/blog-details.html",{
        "blog" : blog
    })
    
def blogs_by_category(request,slug):
    context = {
        "blogs": Category.objects.get(slug=slug).blog_set.filter(is_active=True),
        "categories": Category.objects.all(),
        "selected_category": slug
        
    }
    return render(request,"blog/blogs.html",context)