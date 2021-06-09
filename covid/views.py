from django.shortcuts import render
from django.http import HttpResponse
from distutils import util
from .models import RTG, Patient
from .dl import DeppLearning
import numpy as np


# Create your views here.
def index(request):
    if request.method == 'POST':
        new_Patient = Patient(
            surname = request.POST['surname'],
            name=request.POST['name'],
            date_of_birth=request.POST['date_of_birth'],
            pesel = request.POST['pesel'],
            gender = request.POST['gender'],
        )

        new_Patient.save()
        new_RTG = RTG(
            file=request.FILES['img'],
            patient = new_Patient,
            doctor_diagnose = util.strtobool(request.POST['doctor_diagnose'])
        )

        new_RTG.save()

        dl_model = DeppLearning('media/DL_models/covidApp.h5')
        prediction = dl_model.diagnose(new_RTG.file.url)[0,0]
        prediction = np.exp(prediction)/(1+np.exp(prediction))
        new_RTG.support = round(prediction, 4)
        if prediction < 0.5:
            new_RTG.diagnose = False
            diagnose = 'zdrowy'
            support = round(1 - new_RTG.support, 4)
        else:
            new_RTG.diagnose = True
            diagnose = 'COVID'
            support = round(new_RTG.support, 4)



        new_RTG.save()

        return render(request, 'result.html', {'support': str(support*100)+'%', 'diagnose': diagnose})

    else:
        return render(request, 'index.html')