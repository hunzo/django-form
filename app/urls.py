from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='home'),
    path('add/', views.AddPostView.as_view(), name='add_class_view'),
    path('update/<int:pk>', views.UpdatePostView.as_view(), name='update_class_view')
]

