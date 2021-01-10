from django.urls import path

from chats import views

urlpatterns = [
    path('', views.HomeView.as_view(), name='chats')
]
