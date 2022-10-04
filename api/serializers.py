from rest_framework import serializers
from walletapp.models import Customer

class CustomerSerializer(serializers.ModelSerializer):
    class Meta: 
        model = Customer
        fields = ('first_name', 'last_name', 'email', 'age', 'address',)
