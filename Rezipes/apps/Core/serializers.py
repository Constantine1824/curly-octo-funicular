from rest_framework.serializers import ModelSerializer, ValidationError
from .models import Recipes, Ratings
from apps.Account.serializers import UserSerializer

class RecipeCreateSerializer(ModelSerializer):

    class Meta:
        model = Recipes
        fields = ['title', 'content']

    def create(self, validated_data):
        user = self.context.get('request').user
        print(user)
        instance = self.Meta.model(**validated_data)
        instance.author = user
        instance.save()
        return instance
    
class RecipeSerializer(ModelSerializer):
    author= UserSerializer()
    class Meta:
        model = Recipes
        fields = '__all__'

class RatingSerializer(ModelSerializer):
    class Meta:
        model = Ratings
        fields = ['id', 'recipe', 'rating']

    def create(self, validated_data):
        user = self.context.get('request').user
        instance = self.Meta.model(**validated_data)
        instance.user = user
        instance.save()
        return instance
    
    def update(self, instance, validated_data):
        try:
            if validated_data['rating'] > 5:
                return ValidationError("Rating cannot be greater than 5")
            instance.rating = validated_data['rating']
            instance.save()
            return instance
        except KeyError:
            return ValidationError("rating must be passed in")