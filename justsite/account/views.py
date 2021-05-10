from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth import login, authenticate, logout
from account.forms import CustomUserForm, CustomAuthentication
from base.models import ArticleModel
from account.models import CustomUser


def account(request):
    context = {
        'title':'Signup'
    }

    if request.method == 'POST':
        form = CustomUserForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('signin')
        else:
            context['form'] = form
    else:
        form = CustomUserForm()
        context['form'] = form
    return render(request, 'account/signup.html', context)


def signin(request):
    context = {
        
        
    }
    user = request.user
    if user.is_authenticated:
        return redirect('home')
    
    if request.POST:
        form = CustomAuthentication(request.POST)

        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            
            user = CustomAuthentication(email=email, password=password)

            if user:
                login(request, user)
                return redirect('signin')
    else:
        form = CustomAuthentication()
    
    context['login_form']=form 
    context['title']='Login'

    print(context['login_form'])
    return render(request, 'account/signin.html', context)


def loggingout(request):
    logout(request)
    return redirect('home')
