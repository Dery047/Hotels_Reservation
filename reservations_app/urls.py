from django.urls import path
from .views import auth

urlpatterns = [
    # Autenticación con JWT
    path('register/', auth.RegisterView.as_view(), name='register'),  # POST
    path('token/', auth.MyTokenObtainPairView.as_view(), name='token_obtain_pair'),  # POST
    path('token/refresh/', auth.TokenRefreshView.as_view(), name='token_refresh'),  # POST
]

