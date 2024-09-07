from django.views.generic import ListView, DetailView, CreateView
from .models import Review
from .forms import ReviewForm

class ReviewListView(ListView):
    model = Review
    template_name = 'reviews/review_list.html'

class ReviewDetailView(DetailView):
    model = Review
    template_name = 'reviews/review_detail.html'

class ReviewCreateView(CreateView):
    model = Review
    form_class = ReviewForm
    template_name = 'reviews/create_review.html'
    success_url = '/reviews/'
