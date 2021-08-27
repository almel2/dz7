from django.urls import path

from .views import index, triangle

urlpatterns = [
    path('', index, ),
    path('triangl/', triangle,)
]
