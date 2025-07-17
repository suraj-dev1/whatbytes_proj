from django.urls import path
from .views import DoctorListCreateView, DoctorRetrieveUpdateDeleteView

urlpatterns = [
    path('doctors/', DoctorListCreateView.as_view(), name='doctor-list-create'),
    path('doctors/<int:pk>/', DoctorRetrieveUpdateDeleteView.as_view(), name='doctor-detail'),
]
