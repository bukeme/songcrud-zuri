from rest_framework import serializers
from .models import Artiste, Song


class LyricsInlineSerializer(serializers.Serializer):
	content = serializers.TextField()

class ArtisteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste 
		fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
	artiste_id = serializers.SerializerMethodField(read_only=True)
	lyrics = serializers.SerializerMethodField(read_only=True, many=True)
	class Meta:
		model = Song 
		fields = ['title', 'date_released', 'likes', 'artiste_id', 'lyric']

	def get_artiste_id(self, obj):
		return obj.artiste_id.first_name

	def get_lyric(self, obj):
		qs = obj.lyric_set.all()[:5]
		return LyricsInlineSerializer(qs, many=True, context=self.context)