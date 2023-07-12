from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Evaluation, FinancialData, Indicator, IndicatorValue
from .serializers import Evaluation_Serializer, FinancialData_Serializer, Indicator_Serializer, IndicatorValue_Serializer
from django.shortcuts import get_object_or_404
from .indicators import Indexes

class EvaluationView(APIView):
	def post(self, request):
		data = request.data
		data.update({
			'create_time': timezone.now(),
			'update_time':timezone.now(),
		})
		obj = Evaluation_Serializer(data=data, context={'request': request})
		if obj.is_valid():
			obj.save()
			return Response({'response': 'Evaluation created'}, status=status.HTTP_201_CREATED)
		else:
			return Response({'Error: invalid data or already exist in database'}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id):
		try:
			data = get_object_or_404(Evaluation, id=id)
			dict = data.__dict__
			del dict['_state']
			return Response(dict, status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def put(self, request, id):
		try:	
			data = request.data
			data.update({
				"update_time": timezone.now()
			})
			Evaluation.objects.filter(id=id).update(**data)
			return Response('finished', status=status.HTTP_200_OK)
		except Exception as error:
			print(str(error))
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def delete(self, request, id):
		try:
			Evaluation.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
		



class FinancialDataView(APIView):
	def post(self, request):
		data = request.data
		data.update({
			'create_time': timezone.now(),
			'update_time':timezone.now(),
		})
		obj = FinancialData_Serializer(data=data, context={'request': request}, partial=True)
		if obj.is_valid():
			obj.save()
			return Response({'response': 'Financial Data created'}, status=status.HTTP_201_CREATED)
		else:
			return Response({'Error: invalid data or already exist in database'}, status=status.HTTP_400_BAD_REQUEST)
		
	def get(self, request, id):
			try:
				data = get_object_or_404(FinancialData, id=id)
				dict = data.__dict__
				del dict['_state']
				return Response(dict, status=status.HTTP_302_FOUND)
			except:
				return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, id):
		try:	
			data = request.data
			data.update({
				"update_time": timezone.now()
			})
			FinancialData.objects.filter(id=id).update(**data)
			return Response('finished', status=status.HTTP_200_OK)
		except Exception as error:
			print(str(error))
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def delete(self, request, id):
		try:
			FinancialData.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)




		
class IndicatorView(APIView):
	def post(self, request):
		data = request.data
		data.update({
			'create_time': timezone.now(),
			'update_time':timezone.now(),
		})
		obj = Indicator_Serializer(data=data, context={'request': request})
		if obj.is_valid():
			obj.save()
			return Response({'response': 'Indicator created'}, status=status.HTTP_201_CREATED)
		else:
			return Response({'Error: invalid data or already exist in database'}, status=status.HTTP_400_BAD_REQUEST)
		
	def get(self, request, id):
			try:
				data = get_object_or_404(Indicator, id=id)
				dict = data.__dict__
				del dict['_state']
				return Response(dict, status=status.HTTP_302_FOUND)
			except:
				return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, id):
		try:	
			data = request.data
			data.update({
				"update_time": timezone.now()
			})
			Indicator.objects.filter(id=id).update(**data)
			return Response('finished', status=status.HTTP_200_OK)
		except Exception as error:
			print(str(error))
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def delete(self, request, id):
		try:
			Indicator.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)


class IndicatorValueView(APIView):
	def post(self, request):
		data = request.data
		dic_ind = {}
		for id in data['Indicator_id']:
			indicator = get_object_or_404(Indicator, id=id)
			ind_all = indicator.__dict__
			del ind_all['_state']
			dic_ind.update({
			f'{ind_all["name"]}':ind_all,
			})
				#ind = Indexes(dic_ind, indicator_name)
		finalcial_data = get_object_or_404(Indicator, id=data['FinancialData_id'])
		dict = finalcial_data.__dict__
		del dict['_state']
		inst = Indexes(dict)
		for i in dic_ind.keys():
			inst.load(i)
		con = inst.condiciones()

		return Response({'response': dic_ind, "Result": inst.value, "Especification": inst.respuesta, "condiciones": con}, status=status.HTTP_201_CREATED)

	def get(self, request, id):
			try:
				data = get_object_or_404(IndicatorValue, id=id)
				dict = data.__dict__
				del dict['_state']
				return Response(dict, status=status.HTTP_302_FOUND)
			except:
				return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def put(self, request, id):
		try:	
			data = request.data
			data.update({
				"update_time": timezone.now()
			})
			IndicatorValue.objects.filter(id=id).update(**data)
			return Response('finished', status=status.HTTP_200_OK)
		except Exception as error:
			print(str(error))
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def delete(self, request, id):
		try:
			IndicatorValue.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)	