from django.shortcuts import render
from datetime import datetime
from posts.models import Post
from posts.models import Product
# Create your views here.


def main_page_view(request):
    if request.method == "GET":
        return render(request,'layouts/index.html')
def posts_view(requests):
    if requests.method == "GET":
        posts = Post.objects.all()
        context = {
            'posts': posts
        }

        return render(requests,'posts/posts.html',context=context)

def products_view(request):
    if request.method == 'GET':
        products = Product.objects.all()
        context = {
            'products': products
        }
        return render(request,' products/products.html',context=context)
def products_detail_view(request,id):
    if request.method == "GET":
        product = Product.objects.get(id=id)
        context = {
            "product": product,
            "reviews" : product.review_set.all()

        }

        return render(request,' products/detail.html',context=context)


















