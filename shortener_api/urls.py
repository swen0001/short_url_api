from django.urls import path
from .views import ShortenerAPIView, ShortenerCreateAPIView, ShortenerAPIUpdate, ShortenerDeleteAPIView

app_name = 'shortener_api'

urlpatterns = [
    path('', ShortenerAPIView.as_view(), name='all_links'),
    path('create/', ShortenerCreateAPIView.as_view(), name='create_shortener'),
    path('update/<int:pk>/', ShortenerAPIUpdate.as_view(), name='update_shortener'),
    path('delete/<int:pk>/', ShortenerDeleteAPIView.as_view(), name='delete_shortener'),
]
