from django.shortcuts import render

def index_chat(request):
    return render(request, 'chat/index_chat.html')

def room(request, room_name):
    return render(request, 'chat/room.html', {'room_name': room_name})