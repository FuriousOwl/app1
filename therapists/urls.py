from django.urls import path
from . import views

urlpatterns = [
    path('', views.TherapistListView.as_view(), name='therapist_list'),
    path('<int:pk>/', views.TherapistDetailView.as_view(), name='therapist_detail'),
    path('create/', views.TherapistCreateView.as_view(), name='create_therapist'),
    path('<int:pk>/update/', views.TherapistUpdateView.as_view(), name='update_therapist'),
    path('<int:pk>/delete/', views.TherapistDeleteView.as_view(), name='delete_therapist'),
]
