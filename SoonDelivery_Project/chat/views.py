from django.shortcuts import render, redirect, get_object_or_404
from account.models import User
from delivery.models import delivery_info
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
    new_room.location = get_object_or_404(delivery_info, pk=request.POST["order_id"]).store_location
    new_room.user1 = User.objects.get(id = request.POST["user1_id"]) # 배달자(본인)
    new_room.user2 = User.objects.get(id = request.POST["user2_id"]) # 주문자
    new_room.room_id = request.POST["room_id"]
    new_room.save()
    
    return render(request, 'chat/chat.html', {
      'user_id': new_room.user1_id

    })
  else:
    return render(requset, 'delivery.html')