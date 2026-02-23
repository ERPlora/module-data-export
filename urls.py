from django.urls import path
from . import views

app_name = 'data_export'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('import/', views.import, name='import'),
    path('export/', views.export, name='export'),
    path('settings/', views.settings, name='settings'),
]
