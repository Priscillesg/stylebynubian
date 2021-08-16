from api.models import Favoris
from django.shortcuts import render
from .serializers import FavorisSerializer, UserSerializer
from rest_framework import serializers, viewsets, status
import requests
from django.http import JsonResponse
import os
from dotenv import load_dotenv
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth.models import User
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.views import APIView 
from django.http import HttpResponseBadRequest, HttpResponse
from .models import Favoris
from rest_framework.response import Response



load_dotenv()

# get all businesses
@api_view(['GET'])
def yelp_search(request=None):
    print(request.query_params)
    term =  request.query_params.get('term', None)
    location = request.query_params.get('location', None)
    token = os.environ.get('API_KEY')

    if term is None:
        return HttpResponseBadRequest()


    YELP_SEARCH_ENDPOINT = "https://api.yelp.com/v3/businesses/search"
    headers = {'Authorization': 'Bearer '  + token}
    params = { 'term' :term, 'location' :location}

    r = requests.get(YELP_SEARCH_ENDPOINT, headers=headers, params=params)

    r=r.json()
    print(r)
    data = r.get('businesses')
    

    return JsonResponse(data, safe=False)

# get one businesses
@api_view(["GET"])
def business_detail(request, business_id):
    
    token = os.environ.get('API_KEY')
    YELP_DETAIL_ENDPOINT = "https://api.yelp.com/v3/businesses/{}".format(business_id)
    headers = {"Authorization": "Bearer " + token}

    r = requests.get(YELP_DETAIL_ENDPOINT, headers=headers)
    business_info=r.json()

    return JsonResponse(business_info)

@api_view(["GET"])
def yelp_reviews(request, business_id):
    token = os.environ.get('API_KEY')
    YELP_REVIEWS_ENDPOINT = "https://api.yelp.com/v3/businesses/{}/reviews".format(business_id)
    headers = {"Authorization": "Bearer " + token}

    r = requests.get(YELP_REVIEWS_ENDPOINT, headers=headers)
    business_info=r.json()

    return JsonResponse(business_info)
  



# ----------------------favourites----------------------
@api_view(["GET"])
# @authentication_classes([TokenAuthentication])
# @permission_classes([IsAuthenticated])
def favouritesList(request):
    favourites = Favoris.objects.all()
    serializer = FavorisSerializer(favourites, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def createList(request):
    serializer = FavorisSerializer(data=request.data)
    if serializer.is_valid():
            serializer.save()
    return Response(serializer.data)

@api_view(["DELETE"])
def deleteFavourite(request, pk):
    favourite = Favoris.objects.get(id=pk)
    favourite.delete()
    return Response("Item successfully delete!")



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


