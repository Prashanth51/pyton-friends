from .models import Person
from django.http import HttpResponse
from .models import Person
from django.shortcuts import render, get_object_or_404,get_list_or_404



# Create your views here.
def index(request):
    pList = get_list_or_404(Person)
    return render(request, 'person_index.html', {'pList':pList})

        

def details(request, pid='0'):
    p = get_object_or_404(Person, pk=pid)
    return render(request,'details.html', {'p': p})
        