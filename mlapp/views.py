from django.conf import settings
import os
import pandas as pd
import joblib
import numpy as np
from django.shortcuts import render
from .forms import DrugPredictionForm

MODEL_PATH = os.path.join(settings.BASE_DIR, 'mlapp', 'drug_classifier_rf.pkl')

model = joblib.load(MODEL_PATH)

sex_map = {'Male': 1, 'Female': 0}
bp_map = {'HIGH': 0, 'NORMAL': 1, 'LOW': 2}
cholesterol_map = {'High': 1, 'Normal': 0, 'Low': 2}

def predict_drug(request):
    form = DrugPredictionForm(request.POST or None)
    prediction = None
    error = None

    if request.method == "POST":
        if form.is_valid():
            age = int(form.cleaned_data["age"])
            sex = sex_map[form.cleaned_data["sex"]]
            bp = form.cleaned_data["blood_pressure"]
            cholesterol = cholesterol_map[form.cleaned_data["cholesterol"]]
            na_to_k = float(form.cleaned_data["na_to_k"])

            input_data = np.array([[age, sex, bp, cholesterol, na_to_k]])

            try:
                prediction = model.predict(input_data)[0]
            except Exception as e:
                error = f"Prediction failed: {e}"

    context = {
        'form': form,
        'prediction': prediction,
        'error': error
    }

    return render(request, 'predict.html', context)
