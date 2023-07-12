from django.contrib import admin
from .models import Evaluation, FinancialData, Indicator, IndicatorValue


admin.site.register([Evaluation, FinancialData, Indicator, IndicatorValue])

