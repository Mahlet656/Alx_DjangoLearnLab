from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Let's use 'accounts/' as the prefix for auth, it's conventional
    path('accounts/', include('relationship_app.urls')),
]
