from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from .models import Chat, Contents

def chat(request, user_id = 0):
  if user_id == 0:
    redirect('login')
  
  return render(request, 'chat/chat.html', {
    'user_id': user_id
  })

def room(request, room_name):
    return render(request, 'chat/room.html', {
        'room_name': room_name
    })

def create_room(request, user_id, delivery_owner_id):
  if request.method == 'POST':
    new_room = Chat()
    new_room.user1 = User.objects.get(id=user_id)
    new_room.user2 = User.objects.get(id=delivery_owner_id)
    new_room.room_id = request.POST["room_id"]
    new_room.save()
    return redirect( 'chat', {
      'user_id': user_id
    })
  else:
    return render(requset, 'delivery.html')