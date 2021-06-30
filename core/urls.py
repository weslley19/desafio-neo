from django.urls import include, path
from rest_framework import routers
from .views import ClientViewSet, UserViewSet, AddressViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

router = routers.DefaultRouter()
router.register(r'client', ClientViewSet)
router.register(r'user', UserViewSet)
router.register(r'address', AddressViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
