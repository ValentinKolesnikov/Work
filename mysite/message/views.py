from django.shortcuts import render
from django.middleware import csrf
from django.contrib.auth.models import User
from .models import Chat, Message
from django.http import HttpResponse
import operator

# Create your views here.


def menu(request):
    args = {}
    chats = list(Chat.objects.filter(members__in=[request.user]))
    chats.sort()
    args['chats'] = chats
    return render(request,'message/menu.html', args)

def chat(request, id):
    if request.POST:
        return NewMessage(request, id)
    args = {}
    chat = Chat.objects.filter(members__in=[request.user])
    try:
        chat = chat.get(members__in = [User.objects.get(id=id)])
        args['messages'] = chat.message_set.order_by("date")
    except:
        print('fds')
        chat = []
    args['chat'] = chat
    args['csrf_token'] = csrf.get_token(request)
    return render(request,'message/chat.html', args)

def NewMessage(request, id):
    if request.POST.get('text')=='':
        return HttpResponse('')

    chat = Chat.objects.filter(members__in=[request.user])
    try:
        chat = chat.get(members__in = [User.objects.get(id=id)])
    except:
        chat = Chat()
        chat.save()
        chat.members.add(request.user,User.objects.get(id=id))
    Message.objects.create(chat = chat, user_from = request.user, text = request.POST.get('text'))
    return HttpResponse('')
