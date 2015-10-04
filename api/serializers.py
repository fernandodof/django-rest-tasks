from rest_framework import serializers
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from rest_framework import pagination

from phonebook.models import Person

class PersonSerializer(serializers.ModelSerializer):
	class Meta:
		model = Person
		fields = ('pk', 'name', 'email', 'photo', 'sex', 'birthdate', 'phone')

class PaginatedPersonSerializer(serializers.ModelSerializer):
	def __init__(self, persons, request, num):
		#sex = serializers.SerializerMethodField()
	    paginator = Paginator(persons, num)
	    page = request.query_params.get('page')
	    
	    try:
	        persons = paginator.page(page)
	    except PageNotAnInteger:
	        persons = paginator.page(1)
	    except EmptyPage:
	        persons = paginator.page(paginator.num_pages)
	    count = paginator.count

	    previous = None if not persons.has_previous() else persons.previous_page_number()
	    next = None if not persons.has_next() else persons.next_page_number()
	    serializer = PersonSerializer(persons, many=True)
	    self.data = {'count':count,'previous':previous, 'next':next,'persons':serializer.data}