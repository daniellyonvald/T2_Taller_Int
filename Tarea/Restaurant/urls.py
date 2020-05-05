from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('hamburgesa', views.hamburgesas, name='hamburgesas'),
    path('ingrediente', views.ingredientes, name='ingredientes'),
    path('ingrediente/<int:pk>', views.ingrediente_id, name='ingredientes_id'),
    path('hamburgesa/<int:pk>', views.hamburgesa_id, name='hamburgesas_id'),

]

