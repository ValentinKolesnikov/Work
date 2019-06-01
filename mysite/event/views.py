from django.shortcuts import render,redirect
from django.middleware import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from .forms import CreateEvent, ParticipantForm
from .models import Event, Like, Participant

def activity(request):
    object_list = Event.objects.all()
    object_list = object_list.order_by("-mark")
    paginator = Paginator(object_list, 6)
    page = request.GET.get('page')
    try:
        queryset = paginator.page(page)
    except PageNotAnInteger:
        queryset = paginator.page(1)
    except EmptyPage:
        queryset = paginator.page(paginator.num_pages)
    likes = Like.objects.filter(user = request.user.id)
    args = {'list':queryset, 'likes':likes}
    args['csrf_token'] = csrf.get_token(request)
    return render(request,'event/activity.html', args)

def event(request, id=None):
    if id==0:
        id = -1
    if id:
        try:
            event = Event.objects.get(id=id)
            if request.POST:
                return newparticipant(request, event)
            args = {'event':event}
            args['csrf_token'] = csrf.get_token(request)
            args['form'] = ParticipantForm()
            args['likes'] = Like.objects.filter(user = request.user.id)
            return render(request,'event/event.html', args)
        except:
            args = {'error':True}
            return render(request,'event/event.html', args)
    else:
        return render(request,'event/event.html',args)

def newparticipant(request, event):
        post = request.POST
        participant = Participant()
        if request.FILES:
            photo = request.FILES['photo']
            participant.text = post.get('text','')
            participant.user = request.user
            participant.event = event
            participant.save()
            photo.name = str(Participant.objects.latest('id').id)+'.jpg'
            participant.photo = photo
            participant.save()
        return redirect('/event/'+str(event.id))



def create(request):
    if not request.user.is_authenticated:
        return redirect('/auth/login/')
    user = request.user
    args = {}
    args['csrf_token'] = csrf.get_token(request)
    event = Event()
    form = CreateEvent()

    args['form'] = form

    if request.POST:
        post = request.POST
        if request.FILES:
            photo = request.FILES['photo']
            event.name = post.get('name','')
            event.text = post.get('text','')
            event.user = request.user
            event.save()
            photo.name = str(Event.objects.latest('id').id)+'.jpg'
            event.photo = photo
            event.save()
        return redirect('/event/'+str(user.id))
    return render(request,'event/create.html', args)

@csrf_exempt
def like(request):
    try:
        request.META['HTTP_REFERER']
    except:
        return redirect('/')
    if not request.user.is_authenticated or not request.user.is_staff:
        return redirect(request.META['HTTP_REFERER'])
    else:
        id = request.POST.get('id')
        likes = Like.objects.filter(user = request.user.id)
        if  CheckLike(likes, id):
            r = Event.objects.get(id = id)
            r.mark-=1
            r.save()
            like = Like.objects.filter(user = request.user.id, event = Event.objects.get(id = id))
            like.delete()
        else:
            r = Event.objects.get(id = id)
            r.mark+=1
            r.save()
            like = Like(user = request.user, event = Event.objects.get(id = id))
            like.save()
        return redirect(request.META['HTTP_REFERER'])

def CheckLike(likes, event):
    for like in likes:
        if event == str(like.event.id):
            return True
    return False