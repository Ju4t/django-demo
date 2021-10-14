"""django_test01 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path, re_path
from django.conf import settings
from django.views import static
from item.views import index


def trigger_error(request):
    division_by_zero = 1 / 0


urlpatterns = [
    path(r'', include('api.urls')),
    path(r'async/', index),
    path('admin/', admin.site.urls),
    re_path(r'static/(?P<path>.*)$', static.serve, {'document_root': settings.STATIC_ROOT}),
    path('sentry-debug/', trigger_error)
]
