from django.db import models
from django.db.models.deletion import CASCADE

class Chat():
  # (id)
  user1 = models.ForeignKey('account.User', on_delete=CASCADE, default='')
  user2 = models.ForeignKey('account.User', on_delete=CASCADE, default='')
  last_content = models.CharField(default = 0)
  last_time = models.DateTimeField(default = 0)

class Contents():
  room_id = models.ForeignKey('chat.Chat', on_delete=CASCADE, default='')
  writer = models.ForeignKey('')
  time
  body