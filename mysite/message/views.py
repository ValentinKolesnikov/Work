from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Chat

# Create your views here.


def menu(request):
    args = {}
    args['chats'] = Chat.objects.filter(members__in=[request.user])
    return render(request,'message/menu.html', args)


def chat(request, id):
    args = {}
    chat = Chat.objects.filter(members__in=[request.user])
    chat = chat.filter(members__in = [User.objects.get(id=id)])[0]
    args['chat'] = chat
    args['messages'] = args['chat'].message_set.order_by("date")
    return render(request,'message/chat.html', args)