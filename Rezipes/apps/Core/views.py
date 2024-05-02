from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import RecipeCreateSerializer,RecipeSerializer, RatingSerializer
from .models import Recipes, Ratings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .permissions import IsAuthor, IsRater
from .models import models
from .signals import rate

class AllRecipeAPIView(APIView):
    def get(self, request):
        queryset = Recipes.objects.all()
        serializer = RecipeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class GetPopularRecipes(APIView):
    def get(self, request):
        queryset = Recipes.objects.all().order_by('avg_rating') [:5]
        serializer = RecipeSerializer(queryset, many=True)
        return Response({
            "status":"Success",
            "data" : serializer.data
        }, status=status.HTTP_200_OK)

class ViewRecipe(APIView):
    def get(self, request, id):
        queryset = Recipes.objects.get(id=id)
        serializer = RecipeSerializer(queryset)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CreateRecipeAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request, id=None):
        data = request.data
        print(request.user)
        serializer = RecipeCreateSerializer(data=data, context={"request": request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)    

class EditRecipeAPIView(APIView):
    permission_classes = [IsAuthor]

    def put(self, request, id):
        queryset = Recipes.objects.get(id=id)
        self.check_object_permissions(request, queryset)
        serializer = RecipeSerializer(queryset, data=request.data, partial=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)

    def delete(self, request, id):
        queryset = Recipes.objects.get(id=id)
        self.check_object_permissions(request,queryset)
        queryset.delete()
        return Response(
            status=status.HTTP_204_NO_CONTENT
        )
# Create your views here.

class RateAPIView(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        serializer = RatingSerializer(data=request.data, context={'request' : request})
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            data = {
                "status" : "Success",
                "ratings" : serializer.data,
                "average_rating" : Ratings.objects.filter(recipe=request.data['recipe']).aggregate\
                    (avg_rating = models.Avg('rating'))
            }
            return Response(data,status=status.HTTP_201_CREATED)

    def get(self, request):
        try:
            recipe_id = request.GET['recipe_id']
            recipe_obj = Recipes.objects.get(id=recipe_id)
            total_rate_count = Ratings.objects.filter(recipe=recipe_obj).count()
            avg_rate = Ratings.objects.filter(recipe=recipe_obj).aggregate(avg_rating=models.Avg('rating'))
            data = {
                "total_rating" : total_rate_count,
                "average_rating" : avg_rate
            } 
            return Response(data=data, status=status.HTTP_200_OK)
        except KeyError:
            return Response({
                "status" : "failed",
                "detail" : "recipe id must be provide as query param"
            }, status=status.HTTP_400_BAD_REQUEST)

        except Recipes.DoesNotExist:
            return Response({
                "status" : "failed",
                "detail" : "Invalid id"
            }, status=status.HTTP_400_BAD_REQUEST)
        

class ModifyRatingsAPIView(APIView):
    permission_classes = [IsRater]
    def put(self, request, id):
        try:
            queryset = Ratings.objects.get(id=id)
            self.check_object_permissions(request,queryset)
            serializer = RatingSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(
                    serializer.data,
                    status=status.HTTP_200_OK
                )

        except Ratings.DoesNotExist:
            return Response({
                'status' : "failed",
                "detail" : "The resource is not present on this server"
            }, status=status.HTTP_404_NOT_FOUND)

        except:
            return Response(data={
                "status" : "failed",
                "detail" : "Invalid data"
            }, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        try:
            queryset = Ratings.objects.get(id=id)
            self.check_object_permissions(request,queryset)
            queryset.delete()
            return Response({
                "status" : "success",
                "detail" : "The resource has been deleted "
            }, status=status.HTTP_200_OK)
        except Ratings.DoesNotExist:
            return Response({
                "status" : "failed",
                "detail" : "The resource is not present on this server"
            })
        