from rest_framework import generics, permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import PatientDoctorMapping
from .serializers import PatientDoctorMappingSerializer


class MappingUpdateView(generics.UpdateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [IsAuthenticated]


class MappingListCreateView(generics.ListCreateAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class MappingByPatientView(generics.ListAPIView):
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        patient_id = self.kwargs['patient_id']
        return PatientDoctorMapping.objects.filter(patient__id=patient_id)


class MappingDeleteView(generics.DestroyAPIView):
    queryset = PatientDoctorMapping.objects.all()
    serializer_class = PatientDoctorMappingSerializer
    permission_classes = [permissions.IsAuthenticated]


class AllMappingsByPatientView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        mappings = PatientDoctorMapping.objects.all().order_by('patient')
        serializer = PatientDoctorMappingSerializer(mappings, many=True)
        return Response(serializer.data)
