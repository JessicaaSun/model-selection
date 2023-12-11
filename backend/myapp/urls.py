from django.urls import path, include
from myapp.views import UserInputListCreateView, DatasetListCreateView

urlpatterns = [
    path('api/userinput/', UserInputListCreateView.as_view(), name='userinput-list-create'),
    path('api/dataset/', DatasetListCreateView.as_view(), name='dataset-list-create'),
]
