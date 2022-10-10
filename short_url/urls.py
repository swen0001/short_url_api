from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from shortener_api.views import Redirector

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include('shortener_api.urls', namespace='shortener_api')),
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('<str:short_link>/', Redirector.as_view(), name='redirector'),
]
