from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'pages/home.html')

def shop(request):
    return render(request, 'pages/shop/shop.html')

def about(request):
    return render(request, 'pages/about.html')

def blog(request):
    return render(request, 'pages/blogs/blog.html')

def blogsingle(request):
    return render(request, 'pages/blogs/blogs-single.html')

def contact(request):
    return render(request, 'pages/contact.html')

def cart(request):
    return render(request, 'pages/cart.html')

def checkout(request):
    return render(request, 'pages/shop/checkout.html')

def product(request):
    return render(request, 'pages/shop/single-product.html')

def wishlist(request):
    return render(request, 'pages/shop/wishlist.html')

def single(request):
    return render(request, 'pages/blogs/blogs-single.html')



