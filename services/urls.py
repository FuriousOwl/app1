from django.urls import path
from . import views

urlpatterns = [
    path('', views.home_view, name='home'),
    path('services/', views.ServiceListView.as_view(), name='service_list'),
    path('services/<int:pk>/', views.ServiceDetailView.as_view(), name='service_detail'),
    path('services/create/', views.ServiceCreateView.as_view(), name='create_service'),
    path('services/<int:pk>/update/', views.ServiceUpdateView.as_view(), name='update_service'),
    path('services/<int:pk>/delete/', views.ServiceDeleteView.as_view(), name='delete_service'),
]
