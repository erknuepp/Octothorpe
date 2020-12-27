from django.shortcuts import render

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status
 
from locations.models import Location
from locations.serializers import LocationSerializer
from rest_framework.decorators import api_view


@api_view(['GET', 'POST', 'DELETE'])
def location_list(request):
    # GET list of locations, POST a new location, DELETE all locations
    if request.method == 'GET':
        locations = Location.objects.all()
        
        title = request.GET.get('title', None)
        if title is not None:
            locations = locations.filter(title__icontains=title)
        
        locations_serializer = LocationSerializer(locations, many=True)
        return JsonResponse(locations_serializer.data, safe=False)
        # 'safe=False' for objects serialization
    elif request.method == 'POST':
        location_data = JSONParser().parse(request)
        location_serializer = LocationSerializer(data=location_data)
        if location_serializer.is_valid():
            location_serializer.save()
            return JsonResponse(location_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        count = Location.objects.all().delete()
        return JsonResponse({'message': '{} Locations were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
def location_detail(request, pk):
    # find location by pk (id)
    try: 
        location = Location.objects.get(pk=pk)

        if request.method == 'GET': 
            location_serializer = LocationSerializer(location) 
            return JsonResponse(location_serializer.data)
        elif request.method == 'PUT': 
            location_data = JSONParser().parse(request) 
            location_serializer = LocationSerializer(location, data=location_data) 
            if location_serializer.is_valid(): 
                location_serializer.save() 
                return JsonResponse(location_serializer.data) 
            return JsonResponse(location_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        elif request.method == 'DELETE': 
            location.delete() 
            return JsonResponse({'message': 'Location was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    except Location.DoesNotExist: 
        return JsonResponse({'message': 'The location does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    # GET / PUT / DELETE location
    
        
@api_view(['GET'])
def location_list_published(request):
    # GET all published tutorials
    locations = Location.objects.filter(published=True)
        
    if request.method == 'GET': 
        locations_serializer = LocationSerializer(locations, many=True)
        return JsonResponse(locations_serializer.data, safe=False)
