from django.shortcuts import render

from rest_framework.generics import ListAPIView,ListCreateAPIView,RetrieveAPIView,RetrieveUpdateAPIView,RetrieveUpdateDestroyAPIView
from .serializers  import CarSerializer
# Create your views here.
from .models import Car


class CarListView(ListCreateAPIView):
    queryset=Car.objects.all()
    serializer_class= CarSerializer


class CarDetailView(RetrieveUpdateDestroyAPIView):
    queryset=Car.objects.all()
    serializer_class= CarSerializer