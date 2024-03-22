from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializer import EqualExpenseSerializer
from .services import EqualExpenseService

class EqualExpenseView(APIView):
    def post(self, request):
        serializer = EqualExpenseSerializer(data=request.data)
        if serializer.is_valid():
            EqualExpenseService.create_equal_expense(
                serializer.validated_data['amount'],
                serializer.validated_data['paid_by'],
                serializer.validated_data['splits']
            )
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
