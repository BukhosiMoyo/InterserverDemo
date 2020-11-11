from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('knowledge-base', views.knowledge, name='knowledge'),
    path('knowledge-base/getting-started', views.knowledgeArticle, name='knowledge-article'),

]
