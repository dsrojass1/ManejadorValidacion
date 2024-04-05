from .models import Cliente
from .models import InformacionFinanciera
from .models import Solicitud

from .serializers import ClienteSerializer
from .serializers import InformacionFinancieraSerializer
from .serializers import SolicitudSerializer

from rest_framework import viewsets, permissions

class ClienteViewSet(viewsets.ModelViewSet):
    queryset = Cliente.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = ClienteSerializer
    
class InformacionFinancieraViewSet(viewsets.ModelViewSet):
    queryset = InformacionFinanciera.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = InformacionFinancieraSerializer
    
class SolicitudViewSet(viewsets.ModelViewSet):
    queryset = Solicitud.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = SolicitudSerializer
