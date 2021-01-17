from django.urls import path

from chats import views

urlpatterns = [
    path('', views.ChatListView.as_view(), name='chats'),
    path('create', views.ChatCreateView.as_view(), name='chats-create'),
]
