from django.contrib import admin
from django.urls import path, include
from mainApp.views import AlunosViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
