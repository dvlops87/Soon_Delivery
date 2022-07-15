from django.db import models
from django.db.models.deletion import CASCADE

class Chat(models.Model):
  # id
  # 방번호, 유저1아이디, 유저2아이디, 채팅들(내용, 송신자, 시간)
  location = models.CharField(max_length = 200, default="")
  room_id = models.CharField(max_length = 200, default="")  # 방 id는 주문번호_배달자id로 생성된다.
  user1 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user1')
  user2 = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='user2')
  
  def __str__(slef):
    return str()

class Contents(models.Model):
  room= models.ForeignKey('chat.Chat', on_delete=CASCADE, default='', related_name='room')
  writer = models.ForeignKey('account.User', on_delete=CASCADE, default='', related_name='chat')
  time = models.DateTimeField(auto_now_add=True, blank=True)
  body = models.CharField(max_length = 200, default="")