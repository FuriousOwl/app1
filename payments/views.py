from django.views.generic import ListView, DetailView, CreateView
from .models import Payment
from .forms import PaymentForm

class PaymentListView(ListView):
    model = Payment
    template_name = 'payments/payment_list.html'

class PaymentDetailView(DetailView):
    model = Payment
    template_name = 'payments/payment_detail.html'

class PaymentCreateView(CreateView):
    model = Payment
    form_class = PaymentForm
    template_name = 'payments/process_payment.html'
    success_url = '/payments/'
