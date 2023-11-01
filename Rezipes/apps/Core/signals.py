# from django.db.models.signals import post_save
# from django.dispatch import receiver
# from .models import Ratings, Recipes

# @receiver(post_save, sender=Ratings)
# def rate(sender, instance, created, **kwargs):
#     rate = Ratings.objects.filter(recipe=instance.recipe).aggregate(sum_rating=mod)