from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect

from models import Member
from django.contrib.auth import login, authenticate
from forms import UserCreationForm, MemberCreationForm
from django.db import transaction
from django.contrib import messages
from django.contrib.auth.models import User


@csrf_protect
def member_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        print authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return render(request, "member/member_login.html", {
                'errors': True
            })
    else:
        return render(request, "member/member_login.html", {
            'errors': False
        })


@csrf_protect
def new(request):
    user_form = UserCreationForm(request.POST or None)
    member_form = MemberCreationForm(request.POST or None)
    if request.method == 'POST' and user_form.is_valid() and member_form.is_valid():
        # First we create the user object and hash the password
        user = user_form.save()
        user.set_password(user.password)
        user.save()

        # Then we create the member object and set the user object to it
        member = Member.objects.create(user=user)
        member.phone_number = request.POST['phone_number']
        member.address = request.POST['address']
        member.save()
        messages.success(request, "Your member profile has been created")

        # This is to login the member after he/she has created an account
        auth_user = authenticate(username=user.username, password=user.password)
        if auth_user is not None:
            login(request, user)

        return redirect("/")
    return render(request, 'member/member_form.html', {
        'user_form': user_form,
        'member_form': member_form
    })


@login_required
@transaction.atomic
@csrf_protect
def edit(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        member_form = MemberCreationForm(request.POST, instance=request.user.member)
        if user_form.is_valid() and member_form.is_valid():
            user_form.save()
            member_form.save()
            messages.success(request, "Your profile has successfully been updated")
            return redirect("home:index")
        else:
            messages.error(request, "Please correct the error below")
    else:
        user_form = UserCreationForm(instance=request.user)
        member_form = MemberCreationForm(instance=request.user.member)
    return render(request, 'member/member_form.html', {
        'user_form': user_form,
        'member_form': member_form
    })
