from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('sge_api.urls')),
    path('auth/', include('rest_framework.urls'))
]
