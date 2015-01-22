from rest_framework import authentication, permissions, viewsets

from .models import Sprint, Task
from .serializers import SprintSerializer, TaskSerializer, UserSerializer

class DefaultsMixin(object):
	authentication_classes = (
		authentication.BasicAuthentication,
		authentication.TokenAuthentication
	)
	permission_classes = (
		permissions.IsAuthenticated
	)
	paginate_by = 25
	paginate_by_param = 'page_size'
	max_paginate_by = 100

class SprintViewSet(DefaultsMixin, viewsets.ModelViewSet):
	"""API endpoint for listing and creating sprints"""

	queryset = Sprint.objects.order_by('end')
	serializer_class = SprintSerializer