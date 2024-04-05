from rest_framework import serializers
from .models import Cliente
from .models import InformacionFinanciera
from .models import Solicitud

class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'
        
    
class InformacionFinancieraSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformacionFinanciera
        fields = '__all__'
        
class SolicitudSerializer(serializers.ModelSerializer):
    class Meta:
        model = Solicitud
        fields = '__all__'
        


