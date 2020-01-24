from rest_framework import routers
from .views import AuthorIDViewSet

router = routers.DefaultRouter()
router.register(r'getData', AuthorIDViewSet)

urlpatterns = router.urls