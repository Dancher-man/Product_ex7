from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from django.shortcuts import get_object_or_404
from source.forms import UserReviewForm
from source.models import Product


class CreateReviewView(LoginRequiredMixin, CreateView):
    form_class = UserReviewForm
    template_name = 'reviews/create_review.html'

    def form_valid(self, form):
        product = get_object_or_404(Product, pk=self.kwargs.get('pk'))
        author = self.request.user
        form.instance.author = author
        form.instance.product = product
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('source:product_view', kwargs={'pk': self.object.product.pk})