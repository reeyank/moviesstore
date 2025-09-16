from django.urls import path
from . import views

urlpatterns = [
    path('submit/', views.feedback_submit, name='feedback_submit'),
    path('list/', views.feedback_list, name='feedback_list'),
]
