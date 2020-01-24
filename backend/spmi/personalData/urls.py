from rest_framework import routers
from .views import personalDataViewSet

router = routers.DefaultRouter()
router.register(r'personalData', personalDataViewSet)

urlpatterns = router.urls