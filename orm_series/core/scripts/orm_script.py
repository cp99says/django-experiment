from core.models import Restaurant, Rating, Sale
from django.utils import timezone
from datetime import datetime
from django.db import connection
from django.contrib.auth.models import User


def run():
    restaurant = Restaurant.objects.filter(name__startswith='Hotel Prateek')
    print(restaurant.exists())
    print(restaurant.sales.filter(income__gt=100).values('income', 'restaurant__name'))
    user = User.objects.get(id=1)
    rating, created = Sale.objects.get_or_create(restaurant=restaurant, income=41, datetime=datetime.now())
    for data in restaurant:
        print(data.name)
    print(created)
    print(rating)

