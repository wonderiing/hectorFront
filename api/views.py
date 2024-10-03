from django.shortcuts import render

from rest_framework import viewsets
from app_medica.models import Citas, Medicos, Pacientes, Consultas
from .serializers import ConsultasSerializer, MedicosSerializer, PacientesSerializer, CitasSerializer
# Create your views here.

class ConsultasViewSet(viewsets.ModelViewSet):

    serializer_class = ConsultasSerializer
    queryset = Consultas.objects.all()


class MedicosViewSet(viewsets.ModelViewSet):

    serializer_class = MedicosSerializer
    queryset = Medicos.objects.all()


class PacientesViewSet(viewsets.ModelViewSet):

    serializer_class = PacientesSerializer
    queryset = Pacientes.objects.all()


class CitasViewSet(viewsets.ModelViewSet):

    serializer_class = CitasSerializer
    queryset = Citas.objects.all()
