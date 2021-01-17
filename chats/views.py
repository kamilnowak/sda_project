from django.conf import settings
from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.urls import reverse
from django.views import generic

from chats import models, forms


# class HomeView(View):
#     def get(self, request):
#         return render(request, "chats/index.html")
#

class ChatListView(generic.ListView):
    model = models.Chat
    context_object_name = 'chats'
    template_name = 'chats/index.html'
    queryset = models.Chat.objects.all()

    def get_queryset(self):
        return models.Chat.objects.filter(users__id=self.request.user.id)


class ChatCreateView(generic.CreateView):
    model = models.Chat
    template_name = 'chats/chat_new.html'
    form_class = forms.ChatForm
    success_url = '/'

    def get_form_kwargs(self):
        data = super().get_form_kwargs()
        data['user'] = self.request.user
        return data


