from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import ActivitiesViewSet


router = SimpleRouter()
router.register('api/v1/activities', ActivitiesViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
