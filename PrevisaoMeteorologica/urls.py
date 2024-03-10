from . import views
from django.urls import path

urlpatterns = [   
    path('cidade/<str:cidade>/', views.get_local_clima, name='get_local_clima'),
   
]