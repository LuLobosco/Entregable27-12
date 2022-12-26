from django.shortcuts import render
from django.http import HttpResponse


def view_relatives(request):
    return render(request,'template_familia.html')