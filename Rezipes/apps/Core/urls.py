from django.urls import path, re_path
from .views import (AllRecipeAPIView, ViewRecipe, EditRecipeAPIView,
                     CreateRecipeAPIView, ModifyRatingsAPIView, 
                     RateAPIView, GetPopularRecipes)

urlpatterns = [
    path('all', AllRecipeAPIView.as_view(), name='all-recipes'),
    path('view/<int:id>', ViewRecipe.as_view(), name='view-recipe'),
    path('<uuid:id>/modify', EditRecipeAPIView.as_view(), name='actions'),
    path('create', CreateRecipeAPIView.as_view(), name='create'),
    path('rate', RateAPIView.as_view(), name='rate'),
    path('rate/modify/<uuid:id>', ModifyRatingsAPIView.as_view(), name='modify ratings'),
    path('popular', GetPopularRecipes.as_view(), name='popular')
]
