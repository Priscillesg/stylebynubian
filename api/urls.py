from api.serializers import FavorisSerializer
from django.urls import path, include
from .views import yelp_search, business_detail, UserViewSet, favouritesList, createList, deleteFavourite, yelp_reviews
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
# router.register('favoris', FavorisViewSet, basename='favoris')
# router.register('favoris', favouritesList, basename='favouritesList')

router.register('users', UserViewSet)


urlpatterns = [
    path('api_list/', yelp_search),
    path('api_list/<business_id>', business_detail),
    path('api/', include(router.urls)),
    path('api/favoris/', favouritesList, name='favouritesList'),
    path('api/create-favourites/', createList, name='createList'),
    path('api/favourites-delete/<str:pk>', deleteFavourite, name='deleteFavourite'),
    path('api_list/<business_id>/reviews', yelp_reviews),

]