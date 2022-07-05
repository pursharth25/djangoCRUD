from statistics import mode
from rest_framework import viewsets
from . import models
from . import serializers

class EmployeeViewset(viewsets.ModelViewSet):
    queryset = models.Employee.objects.all()
    serializer_class = serializers.EmployeeSerializer


# creates classes like list(), create(),update(),destroy() for methods POST,GET,PUT,DELETE