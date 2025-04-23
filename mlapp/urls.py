from django.urls import path
from .views import predict_drug

urlpatterns = [
    path("", predict_drug, name="predict_drug"),
]
