from django.urls import include, path
from rest_framework import routers
from .item.viewset import ItemViewSet, CeleryViewSet


router = routers.DefaultRouter()
router.register(r'celery', CeleryViewSet, 'celery')
router.register(r'item', ItemViewSet, 'item')


urlpatterns = [
    path('', include(router.urls)),
]