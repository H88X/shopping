
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect
from .models import Category, Product
from .forms import ProductForm


def index(request):
    text = "dddddhh"
    return HttpResponse(text)


def allProdCat(request):

    product = Product.objects.all()
    category = Category.objects.all()
    context = {'product': product, 'category': category}
    return render(request, 'category.html', context)


def categorydetail(request, category_id):
    products = Product.objects.filter(category_id=category_id)
    context = {'products': products}
    return render(request, 'categorydetail.html', context)




def productdetail(request,Product_id):

    #productdetails = Product.objects.all()
    #return render(request, 'productdetail.html', {'productdetails': productdetails})
    productdetails = Product.objects.get(id=Product_id)
    #products = Product.objects.all()
    context = {'productdetails': productdetails}
    return render(request, 'productdetail.html', context)




def index(request):
    products = Product.objects.order_by('-name')
    context = {'products': products}

    return render(request, 'index.html', context)


def delete(request, product_id):
    productdelete = Product.objects.get(id=product_id)
    productdelete.delete()
    return redirect('/')


def product_create(request):

    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            product = form.save(commit=False)
            product.save()
            return redirect('/')
    else:
        form = ProductForm()
    context = {'form': form}
    return render(request, 'product_form.html', context)







