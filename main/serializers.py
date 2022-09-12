from rest_framework import serializers

from .models import Admin, Client, Order, Status


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = '__all__'


class OrderAdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class StatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = Status
        fields = '__all__'
