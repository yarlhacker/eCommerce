from django.urls import path
from .import views

urlpatterns = [
    path('', views.index , name='index'),
    path('404/', views.error_page , name='error_page'),
    path('about/', views.about , name='about'),
    path('cart/', views.cart , name='cart'),
    path('checkout/', views.checkout , name='checkout'),
    path('contact/',views.contact , name='contact'),
    path('news/',views.news , name='news'),
    path('shop/',views.shop , name='shop'),
    path('single_news/',views.single_news , name='single_news'),
    path('single_product/',views.single_product , name='single_product'),
    
]
