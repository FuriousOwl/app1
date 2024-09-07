from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib import messages
from .models import Service
from .forms import ServiceForm

class ServiceListView(ListView):
    model = Service
    template_name = 'services/service_list.html'
    context_object_name = 'services'

class ServiceDetailView(DetailView):
    model = Service
    template_name = 'services/service_detail.html'
    context_object_name = 'service'

class ServiceCreateView(CreateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/create_service.html'
    success_url = reverse_lazy('service_list')

    def form_valid(self, form):
        messages.success(self.request, 'Service created successfully!')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.error(self.request, 'There was an error creating the service.')
        return super().form_invalid(form)

class ServiceUpdateView(UpdateView):
    model = Service
    form_class = ServiceForm
    template_name = 'services/update_service.html'
    success_url = reverse_lazy('service_list')

class ServiceDeleteView(DeleteView):
    model = Service
    template_name = 'services/delete_service.html'
    success_url = reverse_lazy('service_list')

def home_view(request):
    latest_services = Service.objects.order_by('-id')[:3]
    return render(request, 'home.html', {'latest_services': latest_services})
