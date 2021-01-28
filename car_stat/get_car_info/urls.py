from django.urls import path

from . import views


urlpatterns = [
    path('start/', views.StartView.as_view(), name='start'),

    path('list/<brand>/<model>/', views.InfoView.as_view(), name='info'),

    path('ajax/load-models/', views.load_models, name='ajax_load_models'),
]