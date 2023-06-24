from django.urls import path
from . import views

app_name = 'item'

urlpatterns = [
    path('item/<int:pk>/', views.detail, name='detail'),
    # other URL patterns...
]