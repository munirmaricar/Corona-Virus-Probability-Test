from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def test(request):
    return render(request, 'test.html')

def result(request):
    return render(request, 'result.html')

def prevention(request):
    return render(request, 'prevention.html')