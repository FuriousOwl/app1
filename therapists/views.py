from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Therapist
from .forms import TherapistForm
from django.urls import reverse_lazy

class TherapistListView(ListView):
    model = Therapist
    template_name = 'therapists/therapist_list.html'

class TherapistDetailView(DetailView):
    model = Therapist
    template_name = 'therapists/therapist_detail.html'

class TherapistCreateView(CreateView):
    model = Therapist
    form_class = TherapistForm
    template_name = 'therapists/create_therapist.html'
    success_url = reverse_lazy('therapist_list')

class TherapistUpdateView(UpdateView):
    model = Therapist
    form_class = TherapistForm
    template_name = 'therapists/update_therapist.html'
    success_url = reverse_lazy('therapist_list')

class TherapistDeleteView(DeleteView):
    model = Therapist
    template_name = 'therapists/delete_therapist.html'
    success_url = reverse_lazy('therapist_list')
