"""
Para el taller práctico, construí una pequeña aplicación web que integra todo lo que he aprendido:

• Construcción de la API: Utilicé Django y Django REST Framework para construir una API. 
Esta API simple de Análisis Fundamental, construida con operaciones CRUD. 
 Permite que los usuarios obtengan resultados de indicadores económicos. 
 Los cuales explican, la liquidez, la solvencia, la eficiencia, la rentabilidad y la valuación de una empresa. 
 Esto permitirá al usuario obtener las herramientas suficientes para generar decisiones de compra y 
 venta de acciones a largo plazo, en el mercado bursátil.
"""

"""La siguiente información, es toda la que utilicé para crear el proyecto."""


#Evaluation

#En evaluation POST: 
{
	"name": "ECOPETROL",
	"symbol": "ECOP"
}
#En evaluation GET:

'http://localhost:8080/v1/evaluation/1'


#En evaluation UPDATE:

{
	"name": "TESLA",
	"symbol": "TSLA"
}

#En evaluation DELETE:

'http://localhost:8080/v1/evaluation/1'



#FinancialData

#En financialdata POST:

{
	"evaluation_id": 1,
	"year": 2022,
	"activos_corrientes": 40.917,
	"pasivos_corrientes": 26.709,
	"inventario": 6.52,
	"efectivo": 22.19,
	"deuda_pasivos": 5.75,
	"patrimonio": 54.9,
	"rotacion_inventario": 6.52,
	"ventas": 1313581,
	"activo_fijo": 2.4,
	"beneficio_neto": 0.0,
	"dividendos": 0.0,
	"acciones_totales": 3169504301,
	"precio_acción": 273.47,
	"acciones_propias": 200
}

#En financialdata GET:

'http://localhost:8080/v1/financialdata/1'

#En financialdata UPDATE:

'http://localhost:8080/v1/financialdata/1'
{
	"year": 2021
}

#En financialdata DELET:

'http://localhost:8080/v1/financialdata/1'





# INDICATOR

#En indicator POST:

{
"name": "current_ratio",
"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee liquidamente",
"type_index": "Líquidez",
"formula": "activos_corrientes/pasivos_corrientes"
}
{
"name": "quick_ratio",
"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee liquidamente, a pesar de no vender sus stocks y su inventario",
"type_index": "Líquidez",
"formula": "(activos_corrientes - inventario)/pasivos_corrientes"
}
{
"name": "cash_ratio",
"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee líquidamente",
"type_index": "Líquidez",
"formula": "efectivo/pasivos_corrientes"
}
{
"name": "debt/equity",
"description": "Este indicador entrega el porcentaje de la deuda utilizada para la financiación de la empresa. Responde la siguiente pregunta:¿La empresa esta financiada por deuda o por patrimonio?",
"type_index": "Solvencia",
"formula": "deuda/patrimonio"
}
{
"name": "days_inventory",
"description": "Este indicador determina cuantos dias demora la empresa en renovar su inventario",
"type_index": "Eficiencia",
"formula": "365/rotación_inventario"
}
{
"name": "assets_turnover",
"description": "Este indicador es solo para empresas que no tienen inventario. Determina que tan buena es la empresa usando sus activos para generar ingresos. Es recomendable comparar el assets turnover con mínimo, dos empresas competidoras, para evaluar si el resultado es mayor al promedio",
"type_index": "Eficiencia",
"formula": "ventas/activo_fijo"
}
{
"name": "return_on_equity",
"description": "Este indicador define cuantos dólares de ganancia le corresponden a cada dólar de patrimonio",
"type_index": "Rentabilidad",
"formula": "beneficio_neto/patrimonio"
}
{
"name": "net_margin",
"description": "Este indicador muestra en porcentaje, cuanto del dinero que ingresa a la empresa, se queda en la empresa",
"type_index": "Rentabilidad",
"formula": "beneficio_neto/ventas"
}
{
"name": "earnings_per_share",
"description": "Este indicador determina cuántos dólares beneficio generó la empresa para cada accionista",
"type_index": "Valuación",
"formula": "beneficio_neto-dividendos/acciones_totales"
}
{
"name": "price_earnings_ratio",
"description": "Este indicador determina Cuánto pagan los accionistas por cada dólar de beneficio producido para sus acciones",
"type_index": "Valuación",
"formula": "precio_acción/earnings_per_share"
}
{
"name": "price_to_sales_ratio",
"description": "Este indicador determina Cuánto pagan los accionistas por cada dólar de ventas producido para sus acciones",
"type_index": "Valuación",
"formula": "precio_acción/(ventas/acciones_propias)"
}
{
"name": "book_value",
"description": "Este indicador determina que porcentaje del patrimonio le corresponde a cada acción",
"type_index": "Valuación",
"formula": "patrimonio/acciones_propias"
}

{
"name": "price_to_book_value",
"description": "Este indicador determina cuanto pagan los accionistas por cada dólar propio de la empresa",
"type_index": "Valuación",
"formula": "precio_acción/book_value"
}

#En indicator GET:

'http://localhost:8080/v1/indicator/12'

#En indicator UPDATE:

'http://localhost:8080/v1/indicator/13'

{
"id": 14
}

#En indicator DELETE:

'http://localhost:8080/v1/indicator/13'


#INDICATORVALUE

# Indicatorvalue POST:

{
	"Indicator_id": [1, 2, 3, 4, 5, 6, 7],
	"FinancialData_id": 1
}

#Arrojará esta información:
"""
{
	"response": {
		"current_ratio": {
			"id": 1,
			"name": "current_ratio",
			"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee liquidamente",
			"type_index": "Líquidez",
			"formula": "activos_corrientes/pasivos_corrientes",
			"create_time": "2023-07-13T05:13:43.921001Z",
			"update_time": "2023-07-13T05:13:43.921001Z"
		},
		"quick_ratio": {
			"id": 2,
			"name": "quick_ratio",
			"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee liquidamente, a pesar de no vender sus stocks y su inventario",
			"type_index": "Líquidez",
			"formula": "(activos_corrientes - inventario)/pasivos_corrientes",
			"create_time": "2023-07-13T05:14:00.156411Z",
			"update_time": "2023-07-13T05:14:00.156411Z"
		},
		"cash_ratio": {
			"id": 3,
			"name": "cash_ratio",
			"description": "Este indicador explica la capacidad que tiene una empresa de cubrir sus deudas del corto plazo con lo que posee líquidamente",
			"type_index": "Líquidez",
			"formula": "efectivo/pasivos_corrientes",
			"create_time": "2023-07-13T05:14:22.500272Z",
			"update_time": "2023-07-13T05:14:22.500272Z"
		},
		"debt_equity": {
			"id": 4,
			"name": "debt_equity",
			"description": "Este indicador entrega el porcentaje de la deuda utilizada para la financiación de la empresa. Responde la siguiente pregunta:¿La empresa esta financiada por deuda o por patrimonio?",
			"type_index": "Solvencia",
			"formula": "deuda/patrimonio",
			"create_time": "2023-07-13T05:14:38.898813Z",
			"update_time": "2023-07-13T05:33:39.750083Z"
		},
		"days_inventory": {
			"id": 5,
			"name": "days_inventory",
			"description": "Este indicador determina cuantos dias demora la empresa en renovar su inventario",
			"type_index": "Eficiencia",
			"formula": "365/rotación_inventario",
			"create_time": "2023-07-13T05:15:57.664209Z",
			"update_time": "2023-07-13T05:15:57.664209Z"
		},
		"assets_turnover": {
			"id": 6,
			"name": "assets_turnover",
			"description": "Este indicador es solo para empresas que no tienen inventario. Determina que tan buena es la empresa usando sus activos para generar ingresos. Es recomendable comparar el assets turnover con mínimo, dos empresas competidoras, para evaluar si el resultado es mayor al promedio",
			"type_index": "Eficiencia",
			"formula": "ventas/activo_fijo",
			"create_time": "2023-07-13T05:16:16.885810Z",
			"update_time": "2023-07-13T05:16:16.885810Z"
		},
		"roe": {
			"id": 7,
			"name": "roe",
			"description": "Este indicador define cuantos dólares de ganancia le corresponden a cada dólar de patrimonio",
			"type_index": "Rentabilidad",
			"formula": "beneficio_neto/patrimonio",
			"create_time": "2023-07-13T05:16:30.006709Z",
			"update_time": "2023-07-13T05:47:20.138957Z"
		}
	},
	"Result": {
		"current_ratio": 1.53195552061103,
		"quick_ratio": 1.2878430491594597,
		"cash_ratio": 0.8308060953236738,
		"debt_equity": 0.10473588342440801,
		"days_inventory": 55.98159509202454,
		"assets_turnover": 547325.4166666667,
		"roe": 0.0
	},
	"Especification": {
		"current_ratio": "Se espera que el resultado del indicador sea de al menos 1.5. Esto significaría que la empresa supera con activos a sus pasivos casi por el doble. Es decir, un 50%.",
		"quick_ratio": "Se espera que el resultado del indicador se encuentre por encima de 1.0, para considerar que la empresa sí se mantiene líquida a pesar de no vender su inventario.",
		"cash_ratio": "Se espera que el resultado del indicador se encuentre por encima de 1.0, para considerar que puede pagar sus deudas del corto plazo con lo que tiene actualmente en el banco.",
		"debt_equity": "Se espera que el resultado del indicador se encuentre por debajo de 0.5. Esto quiere decir, que el patrimonio de la empresa supera la deuda.",
		"days_inventory": "Este indicador mostrará, cada cuantos días la empresa renueva su inventario. Entre más grande sea la rotacion de inventario, significa que la empresa renueva el inventario más cantidad de veces por año.",
		"assets_turnover": "Este indicador sirve para comparar la empresa con empresas competidoras. Al hallar el assets turnover de las empresas competidoras. Podrá hacer una comparación con el promedio de todos los assets turnover. Así sabrá que, si su assets turnover esta por encima del promedio de los assets turnover de las demás empresas. Entonces, quiere decir que su empresa rota más veces su activo que las demás empresas, es decir, utiliza correctamente sus activos para generar ingresos.",
		"roe": "Por 0.0 dólar(es) de patrimonio, genera un dólar de ganancia."
	},
	"condiciones": "La empresa evaluada es Solvente. Es decir, que la empresa está financiada mucho más por el patrimonio que por la deuda. Es buena idea comprar acciones de esta empresa, evalua su rentabilidad para mayor seguridad."
}

"""



#USER


#EN user POST:
{
	"user_name": "liyi",
	"password": "afedwef"
}
#En user GET:
'http://localhost:8080/v1/user/1'


#LOGIN

#En login POST:

{
	"user_name": "liyi",
	"password": "afedwef"
}
"""Aparecerá un TOKEN"""
"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6MSwidXNlcl9uYW1lIjoibGl5aSIsInBhc3N3b3JkIjoicGJrZGYyX3NoYTI1NiQzOTAwMDAkVFpSRW9sUkE2eDFyZVBQNHJqYzVBOSR2K01UVkVZTk92VVpSWVVqZmw3MkZJaDR5NVk5bC9JS1BaM0Z5QnRZS1VZPSIsImVtYWlsIjoiIn0.sP42h1Bv_qJUrcLiv90AP4pMV6Hzv3BieIlIOd16Mto"
