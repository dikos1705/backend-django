from django.shortcuts import render 

from .models import Article,Comment
from django.http import Http404,HttpResponseRedirect
from django.urls import reverse

def index(request):
    latest_article_list = Article.objects.order_by('-pub_date')[:5]
    return render(request, 'list.html',{'latest_article_list':latest_article_list})


def detail(request,id):
    try:
        a= Article.objects.get(id=id)
    except:
        raise Http404('Статья не найдена')
    latest_comments_list = a.comment_set.order_by('-id')[:10]
    return render(request, 'detail.html',{'article':a,'latest_comments_list':latest_comments_list})

def leave_comment(request,id):
    try:
        a= Article.objects.get(id=id)
    except:
        raise Http404('Статья не найдена')
    
    a.comment_set.create(author_name=request.POST['name'],comment_text=request.POST['text'])
    
    return HttpResponseRedirect(reverse('articles:detail', args=(a.id,) ) )