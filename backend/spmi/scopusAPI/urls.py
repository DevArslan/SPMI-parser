from rest_framework import routers
from .views import scopusDataViewSet

router = routers.DefaultRouter()
router.register(r'scopusAPI', scopusDataViewSet)

urlpatterns = router.urls