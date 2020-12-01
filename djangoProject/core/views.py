from django.shortcuts import render


def index(request):
    return render(request, 'index.html')

def goAbroad(request):
    return render(request, 'goAbroad.html')

def sumCheck(request):
    value_a = request.POST['valueA']
    value_b = request.POST['valueB']
    result = int(value_a) + int(value_a)
    return render(request, 'sumValue.html', context={'sumValue':result})