from django.db import models
import uuid
from apps.Account.models import User

class BaseModelField(models.Model):
    id = models.UUIDField(default=uuid.uuid4(), primary_key=True)
    time_created = models.DateTimeField(auto_now_add=True)
    time_modified = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

class Recipes(BaseModelField):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    avg_rating = models.DecimalField(default=0.0, decimal_places=1, max_digits=2)


    def __str__(self):
        return self.title
    
    class Meta:
        verbose_name_plural = 'Recipes'

class Comments(BaseModelField):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    recipes = models.ForeignKey(Recipes, on_delete=models.CASCADE)
    text = models.TextField()

    def __str__(self):
        return self.author
    
    class Meta:
        verbose_name_plural = 'Comments'

class BookMark(BaseModelField):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    recipes = models.ManyToManyField(Recipes)

    def __str__(self):
        return self.user.get_username()
    
class Ratings(BaseModelField):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    recipe = models.ForeignKey(Recipes, on_delete=models.CASCADE, related_name='ratings')
    rating = models.IntegerField()

    def __str__(self):
        return self.user.get_username() + " " + self.rating
    
    class Meta:
        verbose_name_plural = 'Ratings'
# Create your models here.
