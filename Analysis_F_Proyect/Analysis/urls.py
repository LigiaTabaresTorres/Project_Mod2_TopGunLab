from django.urls import path
from .views import EvaluationView, FinancialDataView, IndicatorView, IndicatorValueView

urlpatterns = [
  path('evaluation/', EvaluationView.as_view(), name='evaluation'),  
  path('evaluation/<int:id>', EvaluationView.as_view(), name='evaluation'),  
  path('financialdata/', FinancialDataView.as_view(), name='financialdata'),  
  path('financialdata/<int:id>', FinancialDataView.as_view(), name='financialdata'),  
  path('indicator/', IndicatorView.as_view(), name='indicator'),  
  path('indicator/<int:id>', IndicatorView.as_view(), name='indicator'),  
  path('indicatorvalue/', IndicatorValueView.as_view(), name='indicatorvalue'),  
  path('indicatorvalue/<int:id>', IndicatorValueView.as_view(), name='indicatorvalue'),  
]
