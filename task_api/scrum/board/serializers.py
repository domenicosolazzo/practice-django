from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint, Task


# Fetch the user model
User = get_user_model()

class SprintSerializer(serializers.ModelSerializer):
	# Get own links
	links = serializers.SerializerMethodField('get_links')
	request = self.context['request']

	class Meta:
		model = Sprint
		fields = ('id', 'name', 'description', 'end', )

	def get_links(self, obj):
		return {
			'self': reverse('sprint-detail', kwargs={'pk':obj.pk}, request=request)
		}


class TaskSerializer(serializers.ModelSerializer):

	# Show the username of the user (foreign key)
	assigned = serializers.SlugRelatedField(slug_field=User.USERNAME_FIELD, required=False)
	status_display = serializers.serializers.SerializerMethodField('get_status_display')
	links = serializers.SerializerMethodField('get_links')

	request = self.context['request']

	class Meta:
		model = Task
		fields = ('id', 'name', 'description', 'sprint', 'status', 'status_display',
			'order', 'assigned', 'started', 'due', 'completed')

	def get_status_display(self, obj):
		return obj.get_status_display()

	def get_links(self, obj):
		return {
			'self': reverse('task-detail', kwargs={'pk':obj.pk}, request=request)
		}



class UserSerializer(serializers.ModelSerializer):

	full_name = serializers.CharField(source='get_full_name', read_only=True)
	links = serializers.SerializerMethodField('get_links')
	request = self.context['request']

	class Meta:
		model = User
		fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active')

	def get_links(self, obj):
		username = obj.get_username()
		return {
			'self': reverse('user-detail', kwargs={User.USERNAME_FIELD:username}, request=request)
		}
