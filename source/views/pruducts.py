from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from source.forms import ProductForm
from source.models import Product


class ProductsListView(ListView):
    model = Product
    template_name = 'products/index.html'
    context_object_name = 'products'
    paginate_by = 6


class DetailProductView(DetailView):
    model = Product
    template_name = 'products/product_view.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        reviews = self.object.reviews.all()
        if not self.request.user.has_perm('source.view_not_moderated_review'):
            reviews = reviews.filter(is_moderated=True)
        context['reviews'] = reviews.order_by('-created_at')
        return context


class CreateProductView(PermissionRequiredMixin, CreateView):
    form_class = ProductForm
    template_name = 'products/create_product.html'
    permission_required = 'source:create_product'

    def get_success_url(self):
        return reverse('source:product_view', kwargs={'pk': self.object.pk})


class UpdateProductView(PermissionRequiredMixin, UpdateView):
    form_class = ProductForm
    template_name = 'products/update_product.html'
    model = Product
    permission_required = 'source:update_product'

    def get_success_url(self):
        return reverse('source:product_view', kwargs={'pk': self.object.pk})


class DeleteProductView(PermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'products/delete_product.html'
    permission_required = 'source:delete_product'
    success_url = reverse_lazy('source:index')



