from django.shortcuts import render

def home(request):
    return render(request, 'home.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    return render(request, 'register.html')

def knowledge(request):
    return render(request, 'knowledge.html')

def knowledgeArticle(request):
    return render(request, 'knowledge-base-article.html')