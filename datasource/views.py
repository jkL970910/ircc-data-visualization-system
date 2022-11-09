from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from .models import ImmigrationStatusData, CountryData, CategoryData, DestinationData
from django.http import JsonResponse
from rest_framework import status
from .serializer import ImmigrationStatusDataSerializer, CategoryDataSerializer, CountryDataSerializer, DestinationDataSerializer

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def get_immigration(request, data_id):
    if data_id == '*':
        datas = ImmigrationStatusData.objects.all()
        plan_serializer = ImmigrationStatusDataSerializer(datas, many=True)
        return JsonResponse(plan_serializer.data, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        try: 
            data = ImmigrationStatusData.objects.get(id=data_id) 
        except ImmigrationStatusData.DoesNotExist: 
            return JsonResponse({'message': 'The immigration_status_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(data)
        return JsonResponse(immigration_status_data_serializer.data)
    elif request.method == 'PUT':
        immigration_status_data = ImmigrationStatusData.objects.get(id=data_id)
        immigration_status_data_serializer = ImmigrationStatusDataSerializer(instance=immigration_status_data, data=request.data)
        if immigration_status_data_serializer.is_valid():
            immigration_status_data_serializer.save()
            return JsonResponse({'message': 'The immigration_status_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': immigration_status_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            ImmigrationStatusData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The immigration_status_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def get_category(request, data_id):
    datas = CategoryData.objects.all()
    category_data_serializer = CategoryDataSerializer(datas, many=True)
    if data_id == '*':
        datas = CategoryData.objects.all()
        category_data_serializer = CategoryDataSerializer(datas, many=True)
        return JsonResponse(category_data_serializer.data, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        try: 
            data = CategoryData.objects.get(id=data_id) 
        except CategoryData.DoesNotExist: 
            return JsonResponse({'message': 'The category_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        category_data_serializer = CategoryDataSerializer(data)
        return JsonResponse(category_data_serializer.data)
    elif request.method == 'PUT':
        category_data = CategoryData.objects.get(id=data_id)
        category_data_serializer = CategoryDataSerializer(instance=category_data, data=request.data)
        if category_data_serializer.is_valid():
            category_data_serializer.save()
            return JsonResponse({'message': 'The category_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': category_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            CategoryData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The category_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def get_country(request, data_id):
    datas = CountryData.objects.all()
    country_data_serializer = CountryDataSerializer(datas, many=True)
    if data_id == '*':
        datas = CountryData.objects.all()
        country_data_serializer = CountryDataSerializer(datas, many=True)
        return JsonResponse(country_data_serializer.data, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        try: 
            data = CountryData.objects.get(id=data_id) 
        except CountryData.DoesNotExist: 
            return JsonResponse({'message': 'The country_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        country_data_serializer = CountryDataSerializer(data)
        return JsonResponse(country_data_serializer.data)
    elif request.method == 'PUT':
        country_data = CountryData.objects.get(id=data_id)
        country_data_serializer = CountryDataSerializer(instance=country_data, data=request.data)
        if country_data_serializer.is_valid():
            country_data_serializer.save()
            return JsonResponse({'message': 'The country_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': country_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            CountryData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The country_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)

@csrf_exempt
@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes((AllowAny,))
def get_destination(request, data_id):
    datas = DestinationData.objects.all()
    destination_data_serializer = DestinationDataSerializer(datas, many=True)
    if data_id == '*':
        datas = DestinationData.objects.all()
        destination_data_serializer = DestinationDataSerializer(datas, many=True)
        return JsonResponse(destination_data_serializer.data, safe=False, status=status.HTTP_400_BAD_REQUEST)
    else:
        try: 
            data = DestinationData.objects.get(id=data_id) 
        except DestinationData.DoesNotExist: 
            return JsonResponse({'message': 'The destination_data does not exist'}, status=status.HTTP_404_NOT_FOUND)

    # GET, Update, Delete 1 piece of data by id
    if request.method == 'GET':
        destination_data_serializer = DestinationDataSerializer(data)
        return JsonResponse(destination_data_serializer.data)
    elif request.method == 'PUT':
        destination_data = DestinationData.objects.get(id=data_id)
        destination_data_serializer = DestinationDataSerializer(instance=destination_data, data=request.data)
        if destination_data_serializer.is_valid():
            destination_data_serializer.save()
            return JsonResponse({'message': 'The destination_data was updated successfully!'}, status=status.HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({'message': destination_data_serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        try:
            DestinationData.objects.get(id=data_id).delete()
        except Exception as Error:
            return JsonResponse({'message': Error}, status=status.HTTP_400_BAD_REQUEST)
        return JsonResponse({'message': 'The destination_data was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
