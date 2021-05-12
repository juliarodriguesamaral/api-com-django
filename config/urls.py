from django.contrib import admin
from django.urls import path, include
from escola.views import AlunosViewsSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'alunos', AlunosViewsSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]
