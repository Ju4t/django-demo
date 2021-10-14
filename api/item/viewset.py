from rest_framework import viewsets, mixins
from rest_framework_extensions.cache.mixins import CacheResponseMixin
from rest_framework.response import Response
from item.models import Item
from .serializer import ItemSerializer

from django.core.cache import cache
from django.utils.encoding import force_text
from rest_framework_extensions.key_constructor.constructors import (
    DefaultKeyConstructor
)
from rest_framework_extensions.key_constructor.bits import (
    KeyBitBase,
    RetrieveSqlQueryKeyBit,
    ListSqlQueryKeyBit,
    PaginationKeyBit
)
import datetime


class UpdatedAtKeyBit(KeyBitBase):
    def get_data(self, **kwargs):
        key = 'api_updated_at_timestamp'
        value = cache.get(key, None)
        if not value:
            value = datetime.utcnow()
            cache.set(key, value=value)
        return force_text(value)


class CustomObjectKeyConstructor(DefaultKeyConstructor):
    retrieve_sql = RetrieveSqlQueryKeyBit()
    updated_at = UpdatedAtKeyBit()


class CustomListKeyConstructor(DefaultKeyConstructor):
    list_sql = ListSqlQueryKeyBit()
    pagination = PaginationKeyBit()
    updated_at = UpdatedAtKeyBit()


class ItemViewSet(CacheResponseMixin, viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all().order_by('-id')
    serializer_class = ItemSerializer
    # throttle_scope = 'itemDetail'  # 限速


class CeleryViewSet(viewsets.ReadOnlyModelViewSet):

    def list(self, request, *args, **kwargs):
        from item.tasks import add

        for x in range(1000):
            res = add.delay(1, x)
        return Response('111')
