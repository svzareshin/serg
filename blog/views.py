from django.shortcuts import render

from blog.models import BlogArticle


def myview(request):
    posts = BlogArticle.objects.filter(is_published=True)
    return render(request, 'base.html', {'posts': posts})