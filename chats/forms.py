from django import forms
from django.contrib.auth import get_user_model

from chats import models


class ChatForm(forms.ModelForm):
    users = forms.ModelMultipleChoiceField(queryset=get_user_model().objects.all())

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super().__init__(*args, **kwargs)

    def clean_users(self):
        selected_users = self.cleaned_data.get('users')
        if self.user not in selected_users:
            raise forms.ValidationError("You have forgotten about yourself")
        return self

    class Meta:
        model = models.Chat
        fields = ('users',)
