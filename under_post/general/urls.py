import general.views as views
from django.urls import path, re_path
import under_post.settings as settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name='mai_view'),
    path('football/', views.football_view, name='football_view'),
    path('basketball/', views.basketball_view, name='basketball_view'),
    path('history/', views.history_view, name='history_view'),
    path('policy/', views.policy_view, name='policy_view'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
