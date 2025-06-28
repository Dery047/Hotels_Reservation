# Este archivo define las rutas para login, registro, vuelos y hoteles
# IMPORTANTE: usamos 'from .views' porque estamos dentro de la misma app
# Si estuvieras en el urls.py del proyecto, usarías: from reservations_app.views import ...

from django.urls import path
from .views import auth, flights, hotels

urlpatterns = [
    # JWT auth
    path('register/', auth.RegisterView.as_view(), name='register'), #POST
    path('token/', auth.MyTokenObtainPairView.as_view(), name='token_obtain_pair'), #post
    path('token/refresh/', auth.TokenRefreshView.as_view(), name='token_refresh'), #post
]

