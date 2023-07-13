from rest_framework import serializers
from .models import Evaluation, FinancialData, Indicator, IndicatorValue, User

class Evaluation_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Evaluation
    fields = '__all__'
class FinancialData_Serializer(serializers.ModelSerializer):
  class Meta:
    model = FinancialData
    fields = '__all__'

class Indicator_Serializer(serializers.ModelSerializer):
  class Meta:
    model = Indicator
    fields = '__all__'

class IndicatorValue_Serializer(serializers.ModelSerializer):
  class Meta:
    model = IndicatorValue
    fields = '__all__'    
class User_Serializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'    