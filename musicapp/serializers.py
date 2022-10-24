from rest_framework import serializers
from .models import Artiste, Song


class LyricInlineSerializer(serializers.Serializer):
	content = serializers.CharField()

# class LyricSerializer(serializers.Serializer):
# 	content = serializers.CharField(read_only=True)

class SongLikeInlineSerializer(serializers.Serializer):
	username = serializers.CharField(read_only=True)

class ArtisteSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artiste 
		fields = '__all__'


class SongSerializer(serializers.ModelSerializer):
	artiste_id = serializers.SerializerMethodField(read_only=True)
	lyric = serializers.SerializerMethodField()
	likes = serializers.SerializerMethodField(read_only=True)
	date_released = serializers.DateTimeField()
	class Meta:
		model = Song 
		fields = ['title', 'date_released', 'likes', 'artiste_id', 'lyric']

	# def update(self, instance, validated_data):
	# 	print('hello world')
	# 	date_released = validated_data.get('date_released') or None
	# 	if date_released is None:
	# 		date_released = instance.date_released
	# 		validated_data['date_released'] = date_released
	# 	obj = super().update(instance, validated_data)
	# 	return obj


	def get_artiste_id(self, obj):
		return f'{obj.artiste_id.first_name} {obj.artiste_id.last_name}'

	def get_lyric(self, obj):
		qs = obj.lyric_set.all()[:5]
		return LyricInlineSerializer(qs, many=True, context=self.context).data

	def get_likes(self, obj):
		qs = obj.likes.all()
		return SongLikeInlineSerializer(qs, many=True, context=self.context).data