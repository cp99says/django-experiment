from rest_framework import serializers
from .models import Restaurant, Rating, MenuItems, RestaurantItems


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['name', 'price']


class RestaurantSerializer(serializers.ModelSerializer):
    menu_items = MenuItemSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = Restaurant
        fields = ['name', 'website', 'date_opened', 'latitude', 'longitude', 'status', 'restaurant_type', 'menu_items']

    def create(self, validated_data):
        menu_items_data = validated_data.pop('menu_items', [])
        restaurant = Restaurant.objects.create(**validated_data)

        if menu_items_data:
            for item_data in menu_items_data:
                menu_item, created = MenuItems.objects.get_or_create(
                    name=item_data['name'],
                    price=item_data['price']
                )
                RestaurantItems.objects.create(restaurant=restaurant, item=menu_item)

        return restaurant




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def validate_rating(self, value):
        if value < 1 or value > 5:
            print("bhaalu")
            raise serializers.ValidationError("Rating must be between 1 and 5.")
        return value

    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.restaurant = validated_data.get('restaurant', instance.restaurant)
    #     instance.rating = validated_data.get('rating', instance.rating)
    #     print(instance)
    #     return instance
