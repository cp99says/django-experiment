from django.db import models
from django.contrib.auth.models import User


class Restaurant(models.Model):
    class TypeChoices(models.TextChoices):
        INDIAN = 'IN', 'Indian'
        CHINESE = 'CH', 'CHINESE'
        GREEK = 'GR', 'GREEK'
        MEXICAN = 'ME', 'MEXICAN'
        FASTFOOD = 'FA', 'FAST FOOD'
        OTHER = 'OT', 'OTHER'

    class RestaurantStatus(models.TextChoices):
        OPEN = 'O', 'Open'
        CLOSED = 'C', 'Closed'


    name = models.CharField(max_length=100)
    website = models.URLField(max_length=100, default='')
    date_opened = models.DateField()
    latitude = models.FloatField()
    longitude = models.FloatField()
    status = models.CharField(choices = RestaurantStatus.choices, max_length = 100, default = RestaurantStatus.OPEN)
    restaurant_type = models.CharField(max_length=2, choices=TypeChoices.choices)

    # def __str__(self):
    #     return repr(self.name+"  "+self.restaurant_type)
    def get_object(self):
        return self

    class Meta:
        ordering = ['-date_opened']
        indexes = [models.Index(fields=['date_opened', 'name'])]


class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, related_name='ratings')
    rating = models.PositiveIntegerField()

    def __str__(self):
        return repr((self.user, self.restaurant))


class Sale(models.Model):
    restaurant = models.ForeignKey(Restaurant, on_delete=models.SET_NULL, null=True, related_name='sales')
    income = models.DecimalField(max_digits=8, decimal_places=2)
    datetime = models.DateTimeField()
