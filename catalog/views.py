
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.core.exceptions import PermissionDenied
from django.http import HttpResponse
from django.shortcuts import redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, DetailView, TemplateView, CreateView, UpdateView, DeleteView

from catalog.forms import ProductForm
from catalog.models import Product


class HomeView(ListView):
    model = Product
    template_name = "catalog/home.html"
    context_object_name = "products"


class ContactsView(TemplateView):
    template_name = "catalog/contacts.html"

    def post(self, request, *args, **kwargs):
        name = request.POST.get("name")
        message = request.POST.get("message")

        return HttpResponse(f"Спасибо, {name}! Сообщение получено.")


class CatalogDetailView(LoginRequiredMixin, DetailView):
    model = Product
    template_name = "catalog/detail_product.html"
    context_object_name = "product"

    def get_object(self, queryset=None):
        self.product = super().get_object(queryset)
        if self.request.user == self.product.owner:
            return self.product
        else:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")


class CatalogListView(LoginRequiredMixin, ListView):
    model = Product
    template_name = "catalog/catalog_list.html"
    context_object_name = "object_list"
    permission_required = 'catalog.view_product'

    def get_queryset(self):
        queryset = super().get_queryset()
        return queryset.filter(can_unpublish_product=False)


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:catalog_list")
    permission_required = 'catalog.add_product'

    def form_valid(self, form):
        product = form.save()
        user = self.request.user
        product.owner = user
        product.save()
        return super().form_valid(form)


class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'catalog/product_form.html'
    success_url = reverse_lazy("catalog:catalog_list")
    permission_required = 'catalog.change_product'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.user = None

    def form_valid(self, form):
        form.instance.owner = self.request.user
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'catalog/product_delete.html'
    success_url = reverse_lazy("catalog:catalog_list")
    permission_required = 'catalog.delete_product'

    def get_object(self, queryset=None):
        self.product = super().get_object(queryset)
        if (self.request.user == self.product.owner or
                self.request.user.groups.filter(name='Moderator of products').exists()):
            return self.product
        else:
            raise PermissionDenied("Вы не являетесь владельцем этого продукта.")


class CanUnpublishProductView(LoginRequiredMixin, PermissionRequiredMixin, View):
    permission_required = 'catalog.can_unpublish_product'

    def get(self, request, pk):
        product = get_object_or_404(Product, pk=pk)
        product.can_unpublish_product = True
        product.save()
        return redirect('catalog:catalog_list')
