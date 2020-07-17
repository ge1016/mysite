from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from django.urls import reverse
from django.db.models import Q
from .forms import LoginForm,RegForm
from blog.models import Blog


def home(request):
    context = {}
    return render(request,'home.html',context)

def login(request):
    if request.method == 'POST':
        login_form = LoginForm(request.POST)
        if login_form.is_valid():
            user = login_form.cleaned_data['user']
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('home')))
            
    else:
        login_form = LoginForm()

    context = {}
    context['login_form'] = login_form
    return render(request,'login.html',context)

def register(request):
    if request.method == 'POST':
        reg_form = RegForm(request.POST)
        if reg_form.is_valid():
            username = reg_form.cleaned_data['username']
            email = reg_form.cleaned_data['email']
            password = reg_form.cleaned_data['password']
            #创建用户
            user = User.objects.create_user(username,email,password)
            user.save()
            #登录用户
            user = auth.authenticate(username=username,password=password)
            auth.login(request,user)
            return redirect(request.GET.get('from',reverse('home')))
            
    else:
        reg_form = RegForm()

    context = {}
    context['reg_form'] = reg_form
    return render(request,'register.html',context)

def logout(request):
    auth.logout(request)
    return redirect(request.GET.get('from',reverse('home')))

def user_info(request):
    context={}
    return render(request,'user_info.html',context)

def search(request):
    search_words = request.GET.get('wd','').strip()
    #分词 按空格 & | ~
    condition = None
    for word in search_words.split(' '):
        if condition is None:
            condition = Q(title__icontains = word)
        else:
            condition = condition | Q(title__icontains = word)
        
    #筛选 搜索
    search_blogs = []
    if condition is not None:
        search_blogs = Blog.objects.filter(condition)
    

    context = {}
    context['search_words'] = search_words
    context['search_blogs_count'] = search_blogs.count()
    context['search_blogs'] = search_blogs
    return render(request,'search.html',context)
    
        