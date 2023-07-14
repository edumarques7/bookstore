from rest_framework import seralizers

from product.models.category import Category


class CategorySerializer(seralizers.ModelSerializer):
    class Meta:
        model = Category
        fields = [
            'title',
            'slug',
            'description',
            'active',
        ]