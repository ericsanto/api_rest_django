from rest_framework import serializers
from movies.models import Movie
from django.shortcuts import get_object_or_404
from reviews.models import Review
from django.db.models import Avg


class MovieSerializers(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField()

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        reviews = obj.reviews.all().aggregate(
            Avg('stars'))['stars__avg']
        return reviews

    def validate_resume(self, value):
        if len(value) > 200:
            raise serializers.ValidationError(
                'Resumo excedeu o limite máximo de caractere. Limite máximo: 200 caracteres')
        return value

    def validate_title(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                'O título do filme, deve ter, pelo menos, 3 caracteres')
        return value
