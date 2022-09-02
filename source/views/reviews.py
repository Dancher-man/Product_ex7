from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.shortcuts import get_object_or_404
from source.forms import UserReviewForm, ModeratorReviewForm
from source.models import Product, Review


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


class UpdateReviewView(PermissionRequiredMixin, UpdateView):
    form_class = UserReviewForm
    template_name = 'reviews/update_review.html'
    permission_required = 'source.change_review'
    model = Review

    def get_form_class(self):
        if self.request.user.has_perm('source.change_review'):
            return ModeratorReviewForm
        return UserReviewForm

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def form_valid(self, form):
        if not self.request.user.groups.filter(name='moderators').exists():
            form.instance.is_moderated = False
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('source:product_view', kwargs={'pk': self.object.product.pk})


class DeleteReviewView(PermissionRequiredMixin, DeleteView):
    permission_required = 'source.change_review'
    model = Review

    def get(self, request, *args, **kwargs):
        return self.delete(request, *args, **kwargs)

    def has_permission(self):
        return super().has_permission() or self.get_object().author == self.request.user

    def get_success_url(self):
        return reverse('source:product_view', kwargs={'pk': self.object.product.pk})


class ListNotModerateReviewsView(PermissionRequiredMixin, ListView):
    queryset = Review.objects.filter(is_moderated=False)
    model = Review
    template_name = 'reviews/not_moderated_reviews.html'
    context_object_name = 'reviews'
    permission_required = 'source.view_not_moderated_review'