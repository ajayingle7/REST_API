from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Order
from .serializer import OrderSerializer

# Create your views here.


class OrderDetail(APIView):
    def get(self,request):
        obj = Order.objects.all()
        serialzier = OrderSerializer(obj,many=True)
        return Response(serialzier.data,status=status.HTTP_200_OK)

    def post(self,request):
        serializer = OrderSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class OrderInfo(APIView):
    def get(self,request,id):
        try:
            obj = Order.objects.get(id=id)

        except Order.DoesNotExist:
            msg = {"msg":"record not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serializer = OrderSerializer(obj)
        return Response(serializer.data, status=status.HTTP_200_OK)


    def put(self,request,id):
        try:
            obj = Order.objects.get(id=id)

        except Order.DoesNotExist:
            msg = {"msg":"record not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        serilaizer = OrderSerializer(obj,data=request.data)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data,status=status.HTTP_205_RESET_CONTENT)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, id):
        try:
            obj = Order.objects.get(id=id)

        except Order.DoesNotExist:
            msg = {"msg": "record not found"}
            return Response(msg, status=status.HTTP_404_NOT_FOUND)
        serilaizer = OrderSerializer(obj, data=request.data,partial=True)
        if serilaizer.is_valid():
            serilaizer.save()
            return Response(serilaizer.data, status=status.HTTP_205_RESET_CONTENT)
        return Response(serilaizer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,id):
        try:
            obj = Order.objects.get(id=id)

        except Order.DoesNotExist:
            msg = {"msg":"record not found"}
            return Response(msg,status=status.HTTP_404_NOT_FOUND)
        obj.delete()
        return Response({"msg":"record deleted"},status=status.HTTP_204_NO_CONTENT)

