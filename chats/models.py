from django.conf import settings
from django.db import models

# Create your models here.

class Chat(models.Model):
    started = models.DateTimeField('started', editable=False, auto_now_add=True)
    users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='chats')


class Message(models.Model):
    timestamp = models.DateTimeField('timestamp', editable=False, auto_now_add=True)
    chat = models.ForeignKey(Chat, related_name='messages', on_delete=models.CASCADE)
    user_from = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='messages', on_delete=models.CASCADE)
    message_body = models.TextField()

    def save(self, **kwargs):
        super(Message, self).save()
        for user in self.chat.users.all().exclude(id=self.user_from.id):
            if self.chat.user_chat_statuses.get(user=user).status == UserChatStatus.ACTIVE:
                UserMessageStatus.objects.create(user=user, message=self, is_read=True)
            else:
                UserMessageStatus.objects.create(user=user, message=self)


class UserChatStatus(models.Model):
    INACTIVE = 'inactive'
    ACTIVE = 'active'
    ARCHIVED = 'archived'
    CHAT_STATUS_CHOICES = (
        (INACTIVE, 'Inactive'),
        (ACTIVE, 'Active'),
        (ARCHIVED, 'Archived'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_chat_statuses', on_delete=models.CASCADE)
    chat = models.ForeignKey(Chat, related_name='user_chat_statuses', on_delete=models.CASCADE)
    status = models.CharField(max_length=8, choices=CHAT_STATUS_CHOICES, default=ACTIVE)
    joined = models.DateTimeField('joined_timestamp', editable=False, auto_now_add=True)

    class Meta:
        unique_together = (('user', 'chat'),)
        verbose_name_plural = 'user chat statuses'


class UserMessageStatus(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, related_name='user_message_statuses', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='user_message_statuses', on_delete=models.CASCADE)
    is_read = models.BooleanField(default=False)

    class Meta:
        unique_together = ('message', 'user')