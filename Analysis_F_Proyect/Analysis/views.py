from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Evaluation
from .serializers import Evaluation_Serializer, FinancialData_Serializer
from django.shortcuts import get_object_or_404

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
			return Response({'Error: invalid data or alredy exist in database'}, status=status.HTTP_400_BAD_REQUEST)

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