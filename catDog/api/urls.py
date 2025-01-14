from django.urls import path
from .views import AnimalClassifier

urlpatterns = [
    path('predict/', AnimalClassifier.as_view(), name='animal-predict'),
]
