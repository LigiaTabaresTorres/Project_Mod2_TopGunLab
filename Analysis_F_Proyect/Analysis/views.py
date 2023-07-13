from datetime import datetime
from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.utils import timezone
from .models import Evaluation, FinancialData, Indicator, IndicatorValue, User
from .serializers import Evaluation_Serializer, FinancialData_Serializer, Indicator_Serializer, IndicatorValue_Serializer, User_Serializer
from django.shortcuts import get_object_or_404
from .indicators import Indexes
import jwt
from django.contrib.auth.hashers import make_password, check_password
from django.conf import global_settings

class Auth(APIView):
	def OAuth(self, request, *args, **kwargs):
		try:
			json_token = request.META.get('HTTP_AUTHORIZATION')
			validation = jwt.decode(json_token[7:], verify=True, algorithms=['HS256'])
			return validation 
		except:
			raise jwt.InvalidTokenError('Invalid Token')


class EvaluationView(Auth):
	def post(self, request):
		token = self.OAuth(request)
		data = request.data
		data.update({
			'create_time': timezone.now(),
			'update_time':timezone.now(),
		})
		obj = Evaluation_Serializer(data=data, context={'request': request})
		print(data)
		if obj.is_valid():
			Evaluation.objects.create(**data)
			return Response({'response': 'Evaluation created'}, status=status.HTTP_201_CREATED)
		else:
			print()
			return Response({'Error': obj.errors}, status=status.HTTP_400_BAD_REQUEST)

	def get(self, request, id):
		token = self.OAuth(request)
		try:
			data = get_object_or_404(Evaluation, id=id)
			dict = data.__dict__
			del dict['_state']
			return Response(dict, status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def put(self, request, id):
		token = self.OAuth(request)
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
		token = self.OAuth(request)
		try:
			Evaluation.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
		



class FinancialDataView(Auth):
	def post(self, request):
		token = self.OAuth(request)
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
			print(obj.errors())
			return Response({'Error: invalid data or already exist in database'}, status=status.HTTP_400_BAD_REQUEST)
		
	def get(self, request, id):
		token = self.OAuth(request)
		try:
			data = get_object_or_404(FinancialData, id=id)
			dict = data.__dict__
			del dict['_state']
			return Response(dict, status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, id):
		token = self.OAuth(request)
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
		token = self.OAuth(request)
		try:
			FinancialData.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)




		
class IndicatorView(Auth):
	def post(self, request):
		token = self.OAuth(request)
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
			token = self.OAuth(request)
			try:
				data = get_object_or_404(Indicator, id=id)
				dict = data.__dict__
				del dict['_state']
				return Response(dict, status=status.HTTP_302_FOUND)
			except:
				return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

	def put(self, request, id):
		token = self.OAuth(request)
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
		token = self.OAuth(request)
		try:
			Indicator.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)


class IndicatorValueView(Auth):
	def post(self, request):
		token = self.OAuth(request)
		data = request.data
		dic_ind = {}
		for id in data['Indicator_id']:
			indicator = get_object_or_404(Indicator, id=id)
			ind_all = indicator.__dict__
			del ind_all['_state']
			dic_ind.update({
			f'{ind_all["name"]}':ind_all,
			})
				
		finalcial_data = get_object_or_404(FinancialData, id=data['FinancialData_id'])
		dict = finalcial_data.__dict__
		del dict['_state']
		print(dict)
		inst = Indexes(dict)
		for i in dic_ind.keys():
			inst.load(i)
		con = inst.condiciones()

		return Response({'response': dic_ind, "Result": inst.value, "Especification": inst.respuesta, "condiciones": con}, status=status.HTTP_201_CREATED)

	def get(self, request, id):
			token = self.OAuth(request)
			try:
				data = get_object_or_404(IndicatorValue, id=id)
				dict = data.__dict__
				del dict['_state']
				return Response(dict, status=status.HTTP_302_FOUND)
			except:
				return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
	
	def put(self, request, id):
		token = self.OAuth(request)
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
		token = self.OAuth(request)
		try:
			IndicatorValue.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

class UserView(Auth):	
	def post(self, request, id):
		data = request.data
		data.update({
			'password': make_password(data['password']),
			'create_time': timezone.now(),
			'update_time':timezone.now(),
		})
		serializer = User_Serializer(data=data)
		if serializer.is_valid():
			serializer.save()
		return Response({'response': 'Realized'}, status=status.HTTP_201_CREATED)	
	def get(self, request, id):
		token = self.OAuth(request)
		try:
			data = get_object_or_404(User, id=id)
			print(data)
			dict = data.__dict__
			del dict['_state']
			return Response(dict, status=status.HTTP_302_FOUND)
		except Exception as error:
			print(error)
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
		
	def put(self, request, id):
		token = self.OAuth(request)
		try:	
			data = request.data
			data.update({
				"update_time": timezone.now()
			})
			User.objects.filter(id=id).update(**data)
			return Response('finished', status=status.HTTP_200_OK)
		except Exception as error:
			print(str(error))
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)

	def delete(self, request, id):
		token = self.OAuth(request)
		try:
			User.objects.filter(id=id).delete()
			return Response("finished", status=status.HTTP_302_FOUND)
		except:
			return Response({'Error: data not found'}, status=status.HTTP_404_NOT_FOUND)
		
class LoginView(Auth):
	def post(self, request):
		data = request.data

		user = get_object_or_404(User, user_name=data['user_name'])
		user = user.__dict__
		del user['_state']
		del user['create_time']
		del user['update_time']
		user_pass = user['password']

		if check_password(data['password'], user_pass):
			token = jwt.encode(user, global_settings.SECRET_KEY, algorithm='HS256')
		return Response(token, status=status.HTTP_200_OK)