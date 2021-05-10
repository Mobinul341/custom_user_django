from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from account.forms import CustomUserForm
from .models import ArticleModel
from account.models import CustomUser

def index(request):
    blog = ArticleModel.objects.all()
    context = {
        'title':'Article',
        'blog':blog


    }
    return render(request, 'article/article.html', context)





