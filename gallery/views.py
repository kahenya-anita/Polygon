from django.shortcuts import render
from django.http import HttpResponse
import numpy as np
 
def home(request):
    return render(request, 'home.html')