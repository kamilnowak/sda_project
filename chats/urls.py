from django.urls import path, include
from rest_framework import routers

from chats import views

router = routers.DefaultRouter()
router.register(r'chats', views.ChatViewSet, basename='chats')

urlpatterns = [
    path(r'api/', include(router.urls)),
    path('', views.ChatListView.as_view(), name='chats'),
    path('create', views.ChatCreateView.as_view(), name='chats-create'),
]
