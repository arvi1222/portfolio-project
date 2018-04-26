from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
import jobs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', jobs.views.home, name='home'),
    path('blog/', include('blog.urls')),
    path('eda/', jobs.views.eda, name='eda'),
    path('investigate_data_set/', jobs.views.investigate_data_set, name='investigate_data_set'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #so it knows where to find media files
