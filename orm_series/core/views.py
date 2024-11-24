from rest_framework import viewsets
from rest_framework.decorators import action
from .models import Restaurant, Rating
from rest_framework.response import Response
from .serializer import RestaurantSerializer, RatingSerializer

class RestaurantViewSet(viewsets.ModelViewSet):
    queryset = Restaurant.objects.all()
    serializer_class = RestaurantSerializer

    def get_serializer(self, *args, **kwargs):
        fields = self.request.query_params.get('fields')
        if fields:
            fields = fields.split(',')
            kwargs['fields'] = fields
        return super().get_serializer(*args, **kwargs)

    def get_queryset(self):
        queryset = super().get_queryset()
        filters = {}

        for param, value in self.request.query_params.items():
            if value and hasattr(Restaurant, param):
                filters[param] = value

        return queryset.filter(**filters)

    @action(detail=False, methods=['GET'], url_path='top-rated')
    def top_ratings_restaurant(self, request, *args, **kwargs):
        restaurant = Restaurant.objects.filter(rating__gt=3)
        serializer = self.get_serializer(restaurant, many=True)
        return Response(serializer.data)



class RatingViewSet(viewsets.ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer