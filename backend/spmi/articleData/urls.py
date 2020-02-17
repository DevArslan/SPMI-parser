from rest_framework import routers
from .views import articleDataViewSet

router = routers.DefaultRouter()
router.register(r'articleData', articleDataViewSet)

urlpatterns = router.urls