from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.serializers import PortfolioSerializer
from main.models import portfolio

@api_view(['GET'])
def portfolioList(request):
    portfolios = portfolio.objects.all()
    serializer = PortfolioSerializer(portfolios, many=True)
    return Response(serializer.data)