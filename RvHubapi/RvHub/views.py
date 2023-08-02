from django.shortcuts import render
from .models import *
from rest_framework import viewsets
from .serializers import *
from rest_framework.response import Response
from rest_framework.views import status, APIView
from rest_framework.parsers import MultiPartParser, FormParser
import json

# Create your views here.

class Registration(viewsets.ModelViewSet):
    queryset = CandidateInfo.objects.all()
    serializer_class = RegistrationSerializer
    parser_classes = (FormParser,MultiPartParser)

    def create(self, request):
        data_dict = json.loads(request.data['data'])
        data_dict['photo'] = request.data.get('photo','')
        serializer_class = RegistrationSerializer(data = data_dict)
        if serializer_class.is_valid():
            serializer_class.save()
            return Response(
				data = {
					'success':True
				},
				status=status.HTTP_200_OK
			)
        else:
            print(serializer_class.errors)
            return Response(
				data={
					'errors':serializer_class.errors,
					'success':False
				},
				status=status.HTTP_200_OK
			)


