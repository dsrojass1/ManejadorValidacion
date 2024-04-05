from rest_framework import routers
from .api import ClienteViewSet
from .api import InformacionFinancieraViewSet
from .api import SolicitudViewSet

routers = routers.DefaultRouter()

routers.register('api/clientes', ClienteViewSet, 'clientes')
routers.register('api/informacionfinanciera', InformacionFinancieraViewSet, 'informacionfinanciera')
routers.register('api/solicitud', SolicitudViewSet, 'solicitud')

urlpatterns = routers.urls