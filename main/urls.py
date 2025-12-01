from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('threads/<slug:board_slug>/', views.thread_list, name='thread_list'),
    path('threads/<slug:board_slug>/<int:thread_id>/', views.thread_detail, name='thread_detail'),
    path('login/', views.login_view, name='login'),
    path('rules/', views.rules_view, name='rules'),
    path('reports/', views.reports_view, name='reports'),
    path('settings/', views.settings_view, name='settings'),
]