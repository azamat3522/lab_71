from django.urls import path, include
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.routers import DefaultRouter

from .views import LogoutView, QuoteViewSet

router = routers.DefaultRouter()

app_name = 'api_v1'

router = DefaultRouter()
router.register(r'quote', QuoteViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', obtain_auth_token, name='obtain_auth_token'),
    path('logout/', LogoutView.as_view(), name='api_token_delete'),
    path('', include(router.urls))

]