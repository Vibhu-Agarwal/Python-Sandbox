from django.urls import path
from .views import BUpdateAPIView

app_name = 'project_management'

urlpatterns = [
    path('b/<int:pk>/', BUpdateAPIView.as_view(),
         name='update-b')
]
