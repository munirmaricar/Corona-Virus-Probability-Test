from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def result(request):
    # corona_form = CoronaForm()
    # if request.method == "POST":
        # pass
        # corona_form = CoronaForm(request.POST)
        # if corona_form.isValid():
            # corona_form.cleaned_data[]
    return render(request, 'result.html')

def form(request):
    return render(request, 'form.html')