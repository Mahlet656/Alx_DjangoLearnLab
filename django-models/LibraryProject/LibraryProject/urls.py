from django.contrib import admin
from django.urls import path, include  # Make sure 'include' is imported

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # This line tells the project to look in relationship_app.urls
    # for any URL that starts with 'library-app/'
    path('library-app/', include('relationship_app.urls')),
]
