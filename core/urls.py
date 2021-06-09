from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('faq/', views.faq, name='faq'),
    path('come-back-soon/', views.come_back_soon, name='come_back_soon'),

]