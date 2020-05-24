from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .forms import *
from .bayes import *

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def result(request):
    return render(request, 'result.html')

def form(request):
    if request.method == "POST":
        corona_form = CoronaForm(request.POST)
        if corona_form.is_valid():
            new_fever = corona_form.cleaned_data['fever']
            new_cold = corona_form.cleaned_data['cold']
            new_fatigue = corona_form.cleaned_data['fatigue']
            new_cough = corona_form.cleaned_data['cough']
            new_short_breath = corona_form.cleaned_data['short_breath']
            new_met_positive_person = corona_form.cleaned_data['met_positive_person']
            new_countries = corona_form.cleaned_data['countries']
            response = {'fever':new_fever, 'cold':new_cold, 'fatigue':new_fatigue, 'cough':new_cough,
                        'short_breath':new_short_breath, 'met_positive_person':new_met_positive_person, 'countries':new_countries}
            symptoms=[]
            for i in response:
                if(response[i]=="Yes"):
                    symptoms.append("T")
                
                elif(response[i]=="No"):
                    symptoms.append("F")
                
                elif(response[i]=="Not Sure"):
                    symptoms.append("X")
                
                if(i=="countries" and response[i][0]!="None"):
                    symptoms.append("T")
                
                elif(i=="countries" and response[i][0]=="None"):
                    symptoms.append("F")
            
            result = round(inference(symptoms)*100,2)

            return render(request, 'result.html', {'result':result})
    else:
        corona_form = CoronaForm()
    return render(request, 'form.html', {'form':corona_form})