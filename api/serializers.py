from rest_framework import serializers

from phonebook.models import Person

class PersonSerializer(serializers.ModelSerializer):
	sex = serializers.SerializerMethodField()

	class Meta:
		model = Person
		fields = ('pk', 'name', 'email', 'photo', 'sex', 'birthdate', 'phone')

	def get_sex(self,obj):
		return obj.get_sex_display()