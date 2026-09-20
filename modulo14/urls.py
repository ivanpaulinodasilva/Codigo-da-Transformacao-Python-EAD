from django.urls import path
from modulo14 import views

urlpatterns = [
    path('', views.produto_list, name='produto_list'),
    path('novo/', views.produto_create, name='produto_create'),
    path('editar/<int:pk>/', views.produto_update, name='produto_update'),
    path('deletar/<int:pk>/', views.produto_delete, name='produto_delete'),
]

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('modulo14.urls')),
]