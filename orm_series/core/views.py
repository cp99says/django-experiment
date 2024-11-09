from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Restaurant, Rating
from rest_framework.response import Response
from .serializer import RestaurantSerializer, RatingSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    @action(detail=False, methods=['GET'], url_path='top-rated')
    def top_ratings_restaurant(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.filter(rating__gt=3)
        serializer = self.get_serializer(restaurant, many=True)
        return Response(serializer.data)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer