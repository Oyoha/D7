from django.urls import path
from .views import NewsList, NewsFilter, NewsCreateView, NewDetailView, NewDeleteView, NewUpgradeView

urlpatterns = [
    path('', NewsList.as_view()),
    path('<int:pk>', NewDetailView.as_view(), name='new_detail'),
    path('search/', NewsFilter.as_view()),
    path('add/', NewsCreateView.as_view(), name='new_create'),
    path('<int:pk>/edit', NewUpgradeView.as_view(), name='new_upgrade'),
    path('<int:pk>/delete', NewDeleteView.as_view(), name='new_delete'),
]
