from django.shortcuts import render
from django.http import HttpResponse
from family.models import people

def create_familiar(request):
    new_familiar = people.objects.create(name= 'Jazmin', surname = 'Fernandez', age =19, hijos= False)
    print(new_familiar)
    return HttpResponse('Se creo familiar')

def list_relatives(request):
    all_relatives = people.objects.all()
    context = {
        'familiar': all_relatives,
    }
    return render(request,'list_relatives.html', context = context )