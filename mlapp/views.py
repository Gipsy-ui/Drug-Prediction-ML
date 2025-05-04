from django.conf import settings
import os
import pandas as pd
import joblib
import numpy as np
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from .forms import DrugPredictionForm, RegisterForm, LoginForm
import json

MODEL_PATH = os.path.join(settings.BASE_DIR, 'mlapp', 'drug_classifier_rf.pkl')
model = joblib.load(MODEL_PATH)

sex_map = {'Male': 1, 'Female': 0}
bp_map = {'HIGH': 0, 'NORMAL': 1, 'LOW': 2}
cholesterol_map = {'High': 1, 'Normal': 0, 'Low': 2}

def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('predict')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('predict')
            else:
                form.add_error(None, "Invalid username or password")
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')

# === Predict View (Authenticated Only) ===
@login_required(login_url='/login/')
def predict_drug(request):
    form = DrugPredictionForm(request.POST or None)
    prediction = None
    error = None

    if request.method == "POST":
        if form.is_valid():
            try:
                age = int(form.cleaned_data["age"])
                sex = sex_map[form.cleaned_data["sex"]]
                bp = bp_map[form.cleaned_data["blood_pressure"]]
                cholesterol = cholesterol_map[form.cleaned_data["cholesterol"]]
                na_to_k = float(form.cleaned_data["na_to_k"])

                input_data = np.array([[age, sex, bp, cholesterol, na_to_k]])
                prediction = model.predict(input_data)[0]
            except Exception as e:
                error = f"Prediction failed: {e}"

    context = {
        'form': form,
        'prediction': prediction,
        'error': error
    }
    return render(request, 'predict.html', context)

# === Dashboard View (Authenticated Only) ===
@login_required(login_url='/login/')
def dashboard_view(request):
    DATASET_PATH = os.path.join(settings.BASE_DIR, 'mlapp', 'drug200.csv')
    df = pd.read_csv(DATASET_PATH)

    # Get drug counts and convert to native Python types
    target_counts = df['Drug'].value_counts()
    
    context = {
        'total_records': int(df.shape[0]),  # Convert to native int
        'feature_columns_count': int(len(df.columns) - 1),
        'accuracy': 95.0,
        'labels': json.dumps(target_counts.index.tolist()),  # Convert Index to list
        'data': json.dumps(target_counts.values.tolist()),   # Convert numpy array to list
    }
    return render(request, 'dashboard.html', context)