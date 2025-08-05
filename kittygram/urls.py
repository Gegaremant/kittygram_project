# urls.py
from rest_framework.routers import DefaultRouter

from django.urls import include, path

from cats.views import CatViewSet

router = DefaultRouter()

router.register('cats', CatViewSet)
urlpatterns = [
    # Все зарегистрированные в router пути доступны в router.urls
    # Включим их в головной urls.py
    path('', include(router.urls), name='api-root'),
]
