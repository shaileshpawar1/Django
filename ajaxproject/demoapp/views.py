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
from .serializers import StudSerializers
from .models import stud

class StudView(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers


class StudViewCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers
    lookup_field = 'pk'

def StudentView(request):
    if request.method == 'POST':
        rno = request.POST.get("rno")
        name = request.POST.get("name")
        stud.objects.create(rno=rno,name=name)
        return redirect("/")
    else:
        return render(request,"base.html")

