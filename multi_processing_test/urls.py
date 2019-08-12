from django.conf import settings
from django.conf.urls.static import static
from django.urls import path

from . import views

urlpatterns = [
    path('', views.ImportRequestList.as_view(), name="requests"),
    path('requests/<int:pk>/', views.ImportRequestDetail.as_view(), name="request"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
