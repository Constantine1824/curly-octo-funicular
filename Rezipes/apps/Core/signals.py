from django.db.models.signals import post_save
from django.dispatch import receiver
from .models import Ratings, Recipes, models

@receiver(post_save, sender=Ratings)
def rate(sender, instance, created, **kwargs):
    recipe = instance.recipe
    recipe.avg_rating = recipe.ratings.aggregate(models.Avg('rating')) ['rating__avg']
    recipe.save()
