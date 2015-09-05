from rest_framework import serializers
from core import models


class ProductSerializer(serializers.ModelSerializer):

    company = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    category = serializers.SlugRelatedField(
        read_only=True,
        slug_field='name'
    )

    class Meta:
        model = models.Product
        fields = ('name', 'description', 'category', 'company',)
