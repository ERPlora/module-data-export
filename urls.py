from django.urls import path
from . import views

app_name = 'data_export'

urlpatterns = [
    # Dashboard
    path('', views.dashboard, name='dashboard'),

    # Navigation tab aliases
    path('import/', views.data_jobs_list, name='import'),
    path('export/', views.dashboard, name='export'),


    # DataJob
    path('data_jobs/', views.data_jobs_list, name='data_jobs_list'),
    path('data_jobs/add/', views.data_job_add, name='data_job_add'),
    path('data_jobs/<uuid:pk>/edit/', views.data_job_edit, name='data_job_edit'),
    path('data_jobs/<uuid:pk>/delete/', views.data_job_delete, name='data_job_delete'),
    path('data_jobs/bulk/', views.data_jobs_bulk_action, name='data_jobs_bulk_action'),

    # Settings
    path('settings/', views.settings_view, name='settings'),
]
