from django.contrib.auth import get_user_model
from rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Sprint, Task


# Fetch the user model
User = get_user_model()

class SprintSerializer(serializers.ModelSerializer):
	# Get own links
	links = serializers.SerializerMethodField()
	
	class Meta:
		model = Sprint
		fields = ('id', 'name', 'description', 'end', 'links')

	def get_links(self, obj):
		request = self.context['request']

		return {
			'self': reverse('sprint-detail', kwargs={'pk':obj.pk}, request=request)
		}


class TaskSerializer(serializers.ModelSerializer):

	# Show the username of the user (foreign key)
	assigned = serializers.SlugRelatedField(
        slug_field=User.USERNAME_FIELD, required=False, read_only=True)
	status_display = serializers.SerializerMethodField('get_status_display')
	links = serializers.SerializerMethodField()

	
	class Meta:
		model = Task
		fields = ('id', 'name', 'description', 'sprint', 'status', 'status_display',
			'order', 'assigned', 'started', 'due', 'completed', 'links')

	def get_status_display(self, obj):
		return obj.get_status_display()

	def get_links(self, obj):
		request = self.context['request']
		links = {
			'self':reverse('task-detail', kwargs={'pk':obj.pk}, request=request),
			'sprint': None,
			'assigned': None
		}
		if obj.sprint_id:
			links['sprint'] = reverse('sprint-detail', kwargs={'pk': obj.sprint_id}, request=request)
		if obj.assigned:
			links['assigned'] = reverse('user-detail', kwargs={User.USERNAME_FIELD:obj.assigned}, request=request)
		return links



class UserSerializer(serializers.ModelSerializer):

	full_name = serializers.CharField(source='get_full_name', read_only=True)
	links = serializers.SerializerMethodField()

	class Meta:
		model = User
		fields = ('id', User.USERNAME_FIELD, 'full_name', 'is_active','links')

	def get_links(self, obj):
		username = obj.get_username()
		request = self.context['request']

		return {
			'self': reverse('user-detail', kwargs={User.USERNAME_FIELD:username}, request=request)
		}
