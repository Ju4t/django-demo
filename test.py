import os
import sys
import time
import json
import django
import logging

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
django.setup()

from item.models import Item

# 生成一个以当前文件名为名字的logger实例
logger = logging.getLogger(__name__)

if __name__ == '__main__':

    for i in range(900000):
        kws = {
            "title": 'title',
            "content": 'content'
        }
        obj = Item.objects.create(**kws)
        print(obj.id)
