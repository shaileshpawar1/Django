from django.shortcuts import render

from django.db.models import Q, Max
from django.shortcuts import redirect
from django.shortcuts import render, HttpResponse
from django.views.generic import ListView
from django.views.generic import View
from .serializers import *
from .models import *

# Create your views here.
from rest_framework import generics
from .serializers import *
from .models import stud

class StudView(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers


class StudViewCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers
    lookup_field = 'pk'

def StudentView(request):
    return render(request,"base.html")

