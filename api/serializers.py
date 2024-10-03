from rest_framework import serializers

from app_medica.models import Citas, Medicos, Pacientes, Consultas

class CitasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Citas
        fields = '__all__'

class MedicosSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medicos
        fields = '__all__'

class PacientesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pacientes
        fields = '__all__'

class ConsultasSerializer(serializers.ModelSerializer):
    class Meta:
        model = Consultas
        fields = '__all__'