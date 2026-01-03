from django.http import HttpResponse
from django.shortcuts import render

from catalog.models import Product


def home(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/home.html', context=context)


def contacts(request):
    if request.method == "POST":
        name = request.POST.get("name")
        massage = request.POST.get("massage")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")
    return render(request, "catalog/contacts.html")


def view_product(request, product_id):
    product = Product.objects.get(id=product_id)
    context = {
        'product_name': product.name,
        'product_description': product.description,
        'product_category': product.category.name,
        'product_price': product.price,
        'product_created_at': product.created_at,
        'product_updated_at': product.updated_at,
    }
    return render(request, 'catalog/view_product.html', context=context)


def catalog_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'catalog/catalog_list.html', context=context)

# def product_list(request):
#     products = Product.objects.all()
#     context = {
#         'products': products,
#     }
#     return render(request, 'catalog/home.html', context=context)
