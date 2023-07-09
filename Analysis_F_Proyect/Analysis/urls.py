from django.urls import path
from .views import EvaluationView

urlpatterns = [
  path('evaluation/', EvaluationView.as_view(), name='evaluation'),  
  path('evaluation/<int:id>', EvaluationView.as_view(), name='evaluation'),  
]
