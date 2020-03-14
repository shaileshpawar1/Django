from django.contrib.auth import login, logout
from django.db.models import Max
from django.shortcuts import render, redirect
# Create your views here.
from rest_framework import generics

from .forms import *
from .models import *
from .serializers import StudSerializers
from django.contrib.auth.decorators import login_required

class StudView(generics.ListCreateAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers


class StudViewCrud(generics.RetrieveUpdateDestroyAPIView):
    queryset = stud.objects.all()
    serializer_class = StudSerializers
    lookup_field = 'pk'


@login_required
def StudentView(request):
    context = {}
    if request.method == 'POST':
        rno = request.POST.get("rno")
        name = request.POST.get("name")
        img = request.FILES["img"]
        stud.objects.create(rno=rno, name=name, img=img)
        return redirect("/insert")
    if request.method == 'GET':
        maxid = stud.objects.aggregate(Max('id'))
        if maxid['id__max'] == None:
            maxid['id__max'] = 0
        num = maxid['id__max']
        num = num + 1
        context['id'] = num
        return render(request, "insert.html", context)


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
        print("next is auth")
        return redirect('/')

    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            login(request, user)
            print("if next")
            if user:
                if 'next' in request.POST:
                    return redirect(request.POST.get('next'))
                else:
                    print("post/")
                    print(request.POST.get('next'))
                    return redirect("/")

    else:
        form = AccountAuthenticationForm()
    context['login_form'] = form
    print('form')
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


# ########################################################################################

def registration_view1(request):
    context = {}
    if request.POST:
        form = RegistrationForm1(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home1')
        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm1()
        context['registration_form'] = form
    return render(request, 'account/register.html', context)


def logout_view1(request):
    logout(request)
    return redirect('home1')


def login_view1(request):
    context = {}

    user = request.user
    if user.is_authenticated:
        print("next is auth")
        return redirect('home1')

    if request.POST:
        form = AccountAuthenticationForm1(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password)
            login(request, user)

            if user:
                if 'next' in request.POST:
                    print("next post")
                    return redirect(request.POST.get('next'))
                else:
                    print("next /")
                    return redirect("/")

    else:
        form = AccountAuthenticationForm1()

    context['login_form'] = form
    print('form')
    return render(request, "account/login.html", context)


def account_view1(request):
    if not request.user.is_authenticated:
        return redirect("login")

    context = {}
    if request.POST:
        form = AccountUpdateForm1(request.POST, instance=request.user)
        if form.is_valid():
            form.initial = {
                "email": request.POST['email'],
                "username": request.POST['username'],
            }
            form.save()
            context['success_message'] = "Updated"
    else:
        form = AccountUpdateForm1(

            initial={
                "email": request.user.email,
                "username": request.user.username,
            }
        )

    context['account_form'] = form
    return render(request, "account/account.html", context)
