from rest_framework import mixins
from rest_framework import viewsets

from .models import Package
from .serializers import PackageSerializer


class PackageViewSet(viewsets.ModelViewSet):
    """
    This viewset automatically provides `list` and `retrieve` actions.
    """
    queryset = Package.objects.all()
    serializer_class = PackageSerializer
