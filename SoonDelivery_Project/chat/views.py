from django.shortcuts import render, redirect
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

def create_room(request):
  if request.method == 'POST':
    new_room = Chat()
    new_room.last_content = "123"
    # new_room.room_id = request.POST["room_id"]
    new_room.save()
    return render(request, 'chat/chat.html')
  else:
    return render(requset, 'delivery.html')