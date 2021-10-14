import datetime
from django.db import models
from django.core.cache import cache
from django.db.models.signals import post_save, post_delete
from mdeditor.fields import MDTextField


def change_api_updated_at(sender=None, instance=None, *args, **kwargs):
    cache.set('api_updated_at_timestamp', datetime.datetime.utcnow())


# Create your models here.

class Item(models.Model):
    title = models.CharField('标题', max_length=20)
    content = MDTextField('内容', max_length=1000)
    url = models.URLField('网址', null=True)

    # 分表
    SHARDING_TYPE = 'precise'
    SHARDING_COUNT = 10

    class Meta:
        db_table = 'item'
        app_label = 'item'  # 分库


for model in [Item]:
    post_save.connect(receiver=change_api_updated_at, sender=model)
    post_delete.connect(receiver=change_api_updated_at, sender=model)
