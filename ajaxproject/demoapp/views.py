from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics

from .forms import *
from .models import *
from .serializers import StudSerializers


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
        stud.objects.create(rno=rno, name=name)
        return redirect("/")
    else:
        return render(request, "insert.html")


def home_view(request):
    # context={}
    # context['form'] = Account.objects.get()
    return render(request, 'base.html')


def registration_view(request):
    context = {}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        return redirect("home")

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)

            if user:
                login(request, user)
                return redirect("home")

    else:
        form = AccountAuthenticationForm()

    context['login_form'] = form

    # print(form)
    return render(request, "account/login.html", context)


def account_view(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, "account/account.html", context)
