from rest_framework import serializers
from .models import Restaurant, Rating, MenuItems, RestaurantItems


class MenuItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = MenuItems
        fields = ['name', 'price']

class DynamicFieldsModelSerializer(serializers.ModelSerializer):
    def __init__(self, *args, **kwargs):
        fields = kwargs.pop('fields', None)
        super().__init__(*args, **kwargs)

        if fields is not None:
            # Drop any fields not specified in the `fields` argument.
            allowed = set(fields)
            existing = set(self.fields.keys())
            for field_name in existing - allowed:
                self.fields.pop(field_name)

class RestaurantSerializer(DynamicFieldsModelSerializer):
    # menu_items = MenuItemSerializer(many=True, write_only=True, required=False)
    menu_items = serializers.SerializerMethodField()

    class Meta:
        model = Restaurant
        fields = ['name', 'website', 'date_opened', 'latitude', 'longitude', 'status', 'restaurant_type', 'menu_items']

    def get_menu_items(self, obj):
        return RestaurantItems.objects.filter(restaurant=obj).values('item__name', 'price')


    # def create(self, validated_data):
    #     menu_items_data = validated_data.pop('menu_items', [])
    #     restaurant = Restaurant.objects.create(**validated_data)
    #
    #     if menu_items_data:
    #         for item_data in menu_items_data:
    #             menu_item, created = MenuItems.objects.get_or_create(
    #                 name=item_data['name'],
    #             )
    #             RestaurantItems.objects.create(restaurant=restaurant, item=menu_item)
    #
    #     return restaurant




class RatingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = '__all__'
        read_only_fields = ['id', 'created_at', 'updated_at']

    def create(self, validated_data):
        rating_instance = Rating.objects.create(**validated_data)
        try:
            rating_instance.full_clean()
        except:
            serializers.ValidationError(e.message_dict)
        rating_instance.save()
        return rating_instance

    # def update(self, instance, validated_data):
    #     instance.user = validated_data.get('user', instance.user)
    #     instance.restaurant = validated_data.get('restaurant', instance.restaurant)
    #     instance.rating = validated_data.get('rating', instance.rating)
    #     print(instance)
    #     return instance
