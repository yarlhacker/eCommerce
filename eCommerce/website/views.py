from django.shortcuts import render

def index(request):
    return render(request , 'index.html')

def error_page(request):
    return render(request , '404.html')

def about(request):
    return render(request , 'about.html')

def cart(request):
    return render(request , 'cart.html')

def checkout(request):
    return render(request , 'checkout.html')

def contact(request):
    return render(request , 'contact.html')

def news(request):
    return render(request , 'news.html')

def shop(request):
    return render(request , 'shop.html')

def single_news(request):
    return render(request , 'single-news.html')

def single_product(request):
    return render(request , 'single-product.html')


# Create your views here.
