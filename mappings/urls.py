from django.urls import path
from .views import (
    MappingListCreateView,
    MappingUpdateView,
    MappingByPatientView,
    MappingDeleteView,
    AllMappingsByPatientView,  
)

urlpatterns = [
    path('mappings/', MappingListCreateView.as_view(), name='mappings-list-create'),
    path('mappings/<int:pk>/', MappingUpdateView.as_view(), name='mappings-update'),
    path('mappings/patient/<int:patient_id>/', MappingByPatientView.as_view(), name='mappings-by-patient'),
    path('mappings/delete/<int:pk>/', MappingDeleteView.as_view(), name='mappings-delete'),
    

    path('mappings/patient/', AllMappingsByPatientView.as_view(), name='all-mappings-by-patient'),
]
