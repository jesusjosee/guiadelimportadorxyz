from django.urls import path
from . import views

app_name='blog'

urlpatterns = [
    #lista de blogs
    path('', views.home_blog_list, name='home'),
    #blog unico
    path('<int:year>/<int:month>/<int:day>/<slug:post>/', views.blog_detail, name='blog_detail'),
    #path('blog-detail/<id>/', views.blog_detail, name='blog_detail'), #url con id
]