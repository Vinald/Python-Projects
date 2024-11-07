from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return render(request, 'index.html', {'name': 'vinald'})

def add(request):
    var1 = int(request.POST["num1"])
    var2 = int(request.POST["num2"])
    result = var1 + var2
    return render(request, 'result.html', {'result': result, 'num1': var1, 'num2': var2})