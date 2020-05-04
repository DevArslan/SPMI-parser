from rest_framework import routers
from .views import personalDataViewSet
from .views import excelDownloadViewSet
from django.urls import path
from django.conf.urls import url
# router = routers.DefaultRouter()
# router.register(r'personalData', personalDataViewSet)

# url(r'^upload/(?P<filename>[^/]+)$', FileUploadView.as_view())

urlpatterns = [
    path('personalData/', personalDataViewSet.as_view()),
    url(r'^personalData/upload/(?P<filename>[^/]+)$', excelDownloadViewSet.as_view()),
    # path('total_cost/', totalCostViewSet.as_view()),
]

# urlpatterns = router.urls