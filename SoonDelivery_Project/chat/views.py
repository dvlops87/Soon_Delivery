from django.shortcuts import render

def chat(request, user_id = 0):
  if user_id == 0:
    redirect('login')
  
  return render(request, 'chat/chat_list.html')

def room(request, room_name):
  return render (request, 'chat/room.html', {
    'room_name': room_name
  })
