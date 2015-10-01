# from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination

from phonebook.models import Person
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from api.serializers import PersonSerializer, PaginatedPersonSerializer 


@api_view(['GET', 'POST'])
def person_list(request):
    """
    List all people, or create a new person
    """
    if request.method == 'GET':
        people = Person.objects.all()
        serializer = PersonSerializer(people, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        serializer = PersonSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def person_list_paginated(request, search, order):
    """
    Returns a JSON response with a listing of person objects
    """
    search = request.query_params.get('search', None)
    order = request.query_params.get('order', None) 
    print order
    if (search==None):
        search = '';

    if (order == None or order == ''):
        order = 'name'


    people = Person.objects.filter(name__istartswith=search).order_by(order).all()

    paginator = PageNumberPagination()    
    # From the docs:
    # The paginate_queryset method is passed the initial queryset 
    # and should return an iterable object that contains only the 
    # data in the requested page.
    result_page = paginator.paginate_queryset(people, request)
    # Now we just have to serialize the data
    serializer = PersonSerializer(result_page, many=True)
    # From the docs:
    # The get_paginated_response method is passed the serialized page 
    # data and should return a Response instance.
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET', 'PUT', 'DELETE'])
def person_detail(request, pk):
    """
    Get, udpate, or delete a specific person
    """
    try:
        person = Person.objects.get(pk=pk)
    except Person.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PersonSerializer(person)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PersonSerializer(person, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serilizer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        person.delete()
        serializer = PersonSerializer(person)
        return Response(serializer.data)
