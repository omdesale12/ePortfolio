

from rest_framework import serializers
from main.models import portfolio

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = portfolio
        fields = '__all__'  # You can specify the fields you want to include in the response
