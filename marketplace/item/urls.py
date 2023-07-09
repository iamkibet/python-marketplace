from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('', views.items, name='items'),
    path('new/', views.new, name='new'),
    path('item/<int:pk>/', views.detail, name='detail'),
    path('item/<int:pk>/delete/', views.delete, name='delete'),
    path('item/<int:pk>/edit/', views.Edit, name='edit'),
    # other URL patterns...
]