from django.urls import include, path
from rest_framework import routers
from .views import ClientViewSet, UserViewSet, AddressViewSet


router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'user', UserViewSet)
router.register(r'address', AddressViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
