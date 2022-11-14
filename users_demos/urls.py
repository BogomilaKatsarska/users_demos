from django.contrib import admin
from django.urls import path, include

import users_demos

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('users_demos.auth_app.urls'), name='auth'),
]
