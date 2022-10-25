from django.shortcuts import render, get_object_or_404
from .serializers import ArtisteSerializer, SongSerializer
from rest_framework import generics
from rest_framework.response import Response
from rest_framework import mixins
from .models import Artiste, Song

# Create your views here.

class SongAPIView(mixins.RetrieveModelMixin, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
	queryset = Song.objects.all()
	serializer_class = SongSerializer
	lookup_field = 'pk'

	def perform_update(self, serializer):
		date_released = serializer.validated_data.get('date_released') or None
		print(date_released)
		if date_released is None:
			date_released = self.get_object().date_released
		serializer.save(date_released=date_released)
		return super().perform_update(serializer)

	def get(self, request, *args, **kwargs):

		try:
			pk = kwargs['pk']
		except:
			pk = None
		
		if pk is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		return self.create(request, *args, **kwargs)

	def put(self, request, *args, **kwargs):
		obj = get_object_or_404(Song, pk=kwargs['pk'])
		data = request.data
		date_released = data.get('date_released') or None
		title = data.get('title') or None
		if date_released is None:
			date_released = obj.date_released
			data['date_released'] = date_released
		if title is None:
			title = obj.title
			data['title'] = title
		serializer = SongSerializer(data=data, instance=obj)

		if serializer.is_valid(raise_exception=True):
			serializer.save(date_released=date_released)
		return Response(serializer.data)
        

	def delete(self, request, *args, **kwargs):
		return self.destroy(request, *args, **kwargs)

class ArtisteAPIView(mixins.RetrieveModelMixin, mixins.ListModelMixin, generics.GenericAPIView):
	queryset = Artiste.objects.all()
	serializer_class = ArtisteSerializer
	lookup_field = 'pk'

	def get(self, request, *args, **kwargs):
		try:
			pk = kwargs['pk']
		except:
			pk = None
		if pk is not None:
			return self.retrieve(request, *args, **kwargs)
		return self.list(request, *args, **kwargs)

