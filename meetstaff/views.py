from django.shortcuts import render
from staff.models import Staff

def staff_table(request):
	staff_list = Staff.objects.all().order_by('title')
	return render(request, 'meetstaff/meetstaff_page.html', {'staff_list': staff_list})
