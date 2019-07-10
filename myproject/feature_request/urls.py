from .views import index
from django.urls import path

urlpatterns = [
    # path('', RequestListView.as_view(), name='request-index'),
    # path('', RequestCreateView.as_view(), name='request-create'),
    path('', index, name='index')
]
