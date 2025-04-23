from django import forms

class DrugPredictionForm(forms.Form):
    AGE_CHOICES = [(i, i) for i in range(10, 100)]
    SEX_CHOICES = [("0", "Female"), ("1", "Male")]
    BP_CHOICES = [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")]
    CHOLESTEROL_CHOICES = [("0", "Low"), ("1", "Normal"), ("2", "High"), ("3", "Very High")]

    age = forms.ChoiceField(choices=AGE_CHOICES, label="Age")
    sex = forms.ChoiceField(choices=SEX_CHOICES, label="Sex")
    bp = forms.ChoiceField(choices=BP_CHOICES, label="Blood Pressure")
    cholesterol = forms.ChoiceField(choices=CHOLESTEROL_CHOICES, label="Cholesterol")
    na_to_k = forms.FloatField(label="Na to K Ratio", min_value=0.0)

