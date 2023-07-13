from django.db import models
from django.utils import timezone

class Evaluation(models.Model):
	name = models.CharField(max_length=100, unique=False, blank=True)
	symbol = models.CharField(max_length=10, unique=False)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class FinancialData(models.Model):
	evaluation_id = models.ForeignKey(to=Evaluation, on_delete=models.CASCADE, null=False)
	year = models.IntegerField()
	activos_corrientes = models.FloatField(default=0.0)
	pasivos_corrientes = models.FloatField(default=0.0)
	inventario = models.FloatField(default=0.0)
	efectivo = models.FloatField(default=0.0)
	deuda_pasivos = models.FloatField(default=0.0)
	patrimonio = models.FloatField(default=0.0)
	rotacion_inventario = models.FloatField(default=0.0)
	ventas = models.FloatField(default=0.0)
	activo_fijo = models.FloatField(default=0.0)
	beneficio_neto = models.FloatField(default=0.0)
	dividendos = models.FloatField(default=0.0)
	acciones_totales = models.FloatField(default=0.0)
	precio_acción = models.FloatField(default=0.0)
	acciones_propias = models.FloatField(default=0.0)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class Indicator(models.Model):
	name = models.CharField(max_length=100)
	description = models.TextField()
	type_index = models.CharField(max_length=100, null=True)
	formula = models.CharField(max_length=100)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class IndicatorValue(models.Model):
	Indicator_id = models.ManyToManyField(to=Indicator)
	FinancialData_id = models.ForeignKey(to=FinancialData, on_delete=models.CASCADE)
	value = models.FloatField(default=0.0)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()

class User(models.Model):
	user_name = models.CharField(max_length=100, unique=True, blank=True)
	password = models.CharField(max_length=100, unique=True, blank=True)
	email = models.CharField(max_length=100, unique=True, blank=True)
	create_time = models.DateTimeField()
	update_time = models.DateTimeField()




# Explicación del modelo:

# Company: Este modelo representa una empresa y tiene campos como name (nombre de la empresa), symbol (símbolo de la empresa en la bolsa) y description (descripción de la empresa).

# FinancialStatement: Este modelo representa los estados financieros de una empresa en un año determinado. Tiene una relación ForeignKey con Company, lo que indica que un estado financiero pertenece a una empresa específica. Los campos incluyen year (año del estado financiero), statement_type (tipo de estado financiero, como balance general o estado de resultados) y data (campo JSON que almacena los datos específicos del estado financiero).

# Indicator: Este modelo representa un indicador financiero utilizado en el análisis fundamental. Tiene campos como name (nombre del indicador), description (descripción del indicador), formula (fórmula utilizada para calcular el indicador) y source (fuente del indicador).

# IndicatorValue: Este modelo almacena los valores de los indicadores para una empresa en un año determinado. Tiene relaciones ForeignKey con Company e Indicator, indicando que el valor pertenece a una empresa y un indicador específicos. Los campos incluyen year (año del valor del indicador) y value (valor numérico del indicador).

# Estos son solo ejemplos básicos de modelos para una API de análisis fundamental. Dependiendo de los requisitos específicos de tu servicio, es posible que necesites agregar más campos y relaciones a tus modelos. Además, considera añadir índices, restricciones y métodos personalizados según sea necesario para optimizar tu base de datos y facilitar las operaciones de consulta.
