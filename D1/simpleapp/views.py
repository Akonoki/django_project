from django.shortcuts import render
from django.views import View
from datetime import datetime
from django.core.paginator import Paginator
from django.views.generic import ListView, UpdateView, CreateView, DetailView, DeleteView

from .filters import ProductFilter
from .forms import ProductForm
from .models import Product, Category


class Products(ListView):
    model = Product
    template_name = 'products.html'
    context_object_name = 'products'
    ordering = ['-price']
    paginate_by = 1

    def get_context_data(self, **kwargs):  # забираем отфильтрованные объекты переопределяя метод get_context_data у наследуемого класса (привет, полиморфизм, мы скучали!!!)
        context = super().get_context_data(**kwargs)
        context['filter'] = ProductFilter(self.request.GET, queryset=self.get_queryset())  # вписываем наш фильтр в контекст
        return context


class ProductDetailView(DetailView):
    template_name = 'sample_app/product_detail.html'
    queryset = Product.objects.all()


class ProductCreateView(CreateView):
    template_name = 'sample_app/product_create.html'
    form_class = ProductForm


class ProductUpdateView(UpdateView):
    template_name = 'sample_app/product_create.html'
    form_class = ProductForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Product.objects.get(pk=id)


class ProductDeleteView(DeleteView):
    template_name = 'sample_app/product_delete.html'
    queryset = Product.objects.all()
    success_url = '/products/'








# class ProductsList(ListView):
#     model = Product
#     template_name = 'products.html'
#     context_object_name = 'products'
#     queryset = Product.objects.order_by('-id')
#
#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['time_now'] = datetime.utcnow()
#         context['value1'] = None
#         return context
#
# # создаём представление, в котором будут детали конкретного отдельного товара
# class ProductDetail(DetailView):
#     model = Product  # модель всё та же, но мы хотим получать детали конкретно отдельного товара
#     template_name = 'products.html'  # название шаблона будет products.html
#     context_object_name = 'product'

