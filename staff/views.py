from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.decorators.csrf import csrf_protect

from models import Staff
from forms import UserCreationForm, StaffCreationForm
from django.db import transaction
from django.contrib import messages


@csrf_protect
def new(request):
    user_form = UserCreationForm(request.POST or None)
    staff_form = StaffCreationForm(request.POST or None)
    if request.method == 'POST' and user_form.is_valid() and staff_form.is_valid():
        # First we create a user object and hash the password
        user = user_form.save()
        user.set_password(user.password)
        user.save()

        # Then we create the staff object to associate the user object with
        staff = Staff.objects.create(user=user)
        staff.wage = request.POST.get('wage')
        staff.title = request.POST.get('title')
        print request.POST['supervisor']
        staff.save()

        return render(request, "staff/staff_create_success.html", {})

    return render(request, "staff/staff_form.html", {
        'user_form': user_form,
        'staff_form': staff_form
    })



@login_required
@transaction.atomic
@csrf_protect
def edit(request):
    if request.method == 'POST':
        user_form = UserCreationForm(request.POST, instance=request.user)
        staff_form = StaffCreationForm(request.POST, instance=request.user.staff)
        if user_form.is_valid() and staff_form.is_valid():
            user_form.save()
            staff_form.save()
            messages.success(request, "Your profile has successfully been updated")
            return redirect("home:index")
        else:
            messages.error(request, "Please correct the error below")
    else:
        user_form = UserCreationForm(instance=request.user)
        staff_form = StaffCreationForm(instance=request.user.staff)
    return render(request, 'staff/staff_form.html', {
        'user_form': user_form,
        'staff_form': staff_form
    })
