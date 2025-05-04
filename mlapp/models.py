from django.db import models
from django.contrib.auth.models import User

class PredictionRecord(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    age = models.IntegerField()
    sex = models.CharField(max_length=10)
    bp = models.CharField(max_length=10, verbose_name="Blood Pressure")
    cholesterol = models.CharField(max_length=10)
    na_to_k = models.FloatField(verbose_name="Na to K Ratio")
    predicted_drug = models.CharField(max_length=20)
    confidence = models.FloatField(help_text="Prediction confidence percentage")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"Prediction for {self.user.username} on {self.timestamp.strftime('%Y-%m-%d %H:%M')}"
    
    class Meta:
        ordering = ['-timestamp']
        verbose_name = "Drug Prediction"
        verbose_name_plural = "Drug Predictions"
        
# Create your models here.
