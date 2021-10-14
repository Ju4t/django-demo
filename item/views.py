from django.http import HttpResponse
from item.tasks import add


async def index(request):
    for x in range(50000):
        res = add.delay(1, x)
    return HttpResponse("Hello, async Django!")
