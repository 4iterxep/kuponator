from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
from . import views
from .views import SearchResultsView

urlpatterns = [
    path('', views.home, name='kupons'),
    path('search/', SearchResultsView.as_view(), name='search_results'),
    path('<int:pk>', views.KuponDetailView.as_view(), name='kupon_detail')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
