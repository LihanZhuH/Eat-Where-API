from django.shortcuts import render, get_object_or_404

from django.http import HttpResponse

from django.http import JsonResponse
from rest_framework.views import APIView

from .models import Restaurant

from .models import Restaurant
# from .serializers import RestaurantSerializer
# from rest_framework import viewsets

def index(request):
    return HttpResponse("Hello world!")

class CallModel(APIView):
    def get(self, request):
        r = get_object_or_404(Restaurant, pk=1)
        # r = Restaurant(id=1, name='test', category='12', rating=5)
        response = {'id': r.id,
                    'name': r.name,
                    'category': r.category,
                    'rating': r.rating}
        return JsonResponse(response)

# class RestaurantViewSet(viewsets.ModelViewSet):
#     queryset = Restaurant.objects.all()
#     serializer_class = RestaurantSerializer