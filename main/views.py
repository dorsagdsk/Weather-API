from django.shortcuts import render
from django.contrib.auth.decorators import login_required
# Create your views here.

def login_page(request):
    return render(request, 'login.html')



@login_required
def cities_list_view(request):
    return render(request, 'cities_list.html')