from . import views
from django.urls import path

urlpatterns = [

    path('', views.home, name='home'),
    path('delete/<int:tid>/', views.delete, name='delete'),
    path('update/<int:tid>/',views.update,name='update'),
]
