from django.shortcuts import render,redirect
from django.middleware import csrf
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, HttpRequest
from .forms import CreateWork
from .models import Work, Like

def activity(request):
    object_list = Work.objects.all()
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
    return render(request,'work/activity.html', args)

def work(request, id=None):
    if id==0:
        id = -1
    if id:
        try:
            work = Work.objects.get(id=id)
            args = {'work':work}
            args['csrf_token'] = csrf.get_token(request)
            args['likes'] = Like.objects.filter(user = request.user.id)
            return render(request,'work/work.html', args)
        except:
            args = {'error':True}
            return render(request,'work/work.html', args)
    else:
        return render(request,'work/work.html',args)



def create(request):
    args = {}
    args['csrf_token'] = csrf.get_token(request)
    work = Work()
    form = CreateWork()

    args['form'] = form

    if request.POST:
        post = request.POST
        if request.FILES:
            photo = request.FILES['photo']
            work.name = post.get('name','')
            work.text = post.get('text','')
            if request.user.is_authenticated:
                work.user = request.user
            else:
                work.user = User.objects.get(id=3)
                work.fio = post.get('fio','')
            work.save()
            photo.name = str(Work.objects.latest('id').id)+'.jpg'
            work.photo = photo
            work.save()
        return redirect('/work/'+str(Work.objects.latest('id').id))
    return render(request,'work/create.html', args)

@csrf_exempt
def like(request):
    try:
        request.META['HTTP_REFERER']
    except:
        return redirect('/')
    if not request.user.is_authenticated or not request.user.is_staff:
        return HttpResponse(' ')
    else:
        id = request.POST.get('id')
        likes = Like.objects.filter(user = request.user.id)
        if  CheckLike(likes, id):
            r = Work.objects.get(id = id)
            r.mark-=1
            r.save()
            like = Like.objects.filter(user = request.user.id, work = Work.objects.get(id = id))
            like.delete()
        else:
            r = Work.objects.get(id = id)
            r.mark+=1
            r.save()
            like = Like(user = request.user, work = Work.objects.get(id = id))
            like.save()
        return HttpResponse('')

def CheckLike(likes, work):
    for like in likes:
        if work == str(like.work.id):
            return True
    return False