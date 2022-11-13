from django.shortcuts import render

from django.http import HttpResponse
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http.response import JsonResponse
from rest_framework import status
from . models import products
from . serializers import productsSerializer
from rest_framework.decorators import api_view

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
# Create your views here.

@api_view(['GET', 'POST', 'DELETE'])
def productsList(request):
    if request.method == 'GET':
        products1 = products.objects.all()
        serializer = productsSerializer(products1, many=True)
        return JsonResponse(serializer.data, safe=False)
        #return Response(serializer.data)

    elif request.method == 'POST':
        products_data = JSONParser().parse(request)
        serializer = productsSerializer(data=products_data)
        #serializer = productsSerializer(products1, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = products.objects.all().delete()
        return JsonResponse({'message': '{} Products were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

@api_view(['GET', 'PUT', 'DELETE'])
def productsDetail(request, pk):
    try: 
        product = products.objects.get(pk=pk) 
    except products.DoesNotExist: 
        return JsonResponse({'message': 'The product does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        serializer = productsSerializer(product) 
        return JsonResponse(serializer.data) 
 
    elif request.method == 'PUT': 
        products_data = JSONParser().parse(request) 
        serializer = productsSerializer(product, data=products_data) 
        if serializer.is_valid(): 
            serializer.save() 
            return JsonResponse(serializer.data) 
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        product.delete() 
        return JsonResponse({'message': 'Product was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
        
@api_view(['GET'])
def productsListPublished(request):
    all_products = products.objects.filter(published=True)
        
    if request.method == 'GET': 
        serializer = productsSerializer(all_products, many=True)
        return JsonResponse(serializer.data, safe=False)
