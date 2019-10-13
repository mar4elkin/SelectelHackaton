from django.views.generic.base      import TemplateView
from django.views.generic           import View
from django.shortcuts               import render, get_object_or_404, redirect
from django.template                import loader, RequestContext
from django.urls                    import reverse
from django.http                    import JsonResponse, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf   import csrf_protect
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models               import Q
#from django.contrib.postgres.search import SearchVector


import                                     datetime

from selectelhackaton.coreApp.models     import Task, Squad
from selectelhackaton.coreApp.forms import MainTaskForm
from taggit.models import Tag, TaggedItem

@login_required
def list_task(request):
    if not request.user.is_staff:
        return HttpResponseNotFound
    task_list = []
    for task in Task.objects.all():
        if task.is_available(request.user):
            task_list.append(task)

    context = {
        'task_list':task_list
    }


    return render(request, 'coreApp/tasks-list.html', context)

@login_required
def add_task(request):
    context = dict()
    context['form'] = MainTaskForm()
    context['tag_list'] = Tag.objects.all()

    if request.method == "POST":
        data = request.POST
        context['form'] = MainTaskForm(data)



        print(dict(data))
        # # data validate

        task = Task.objects.create(
            author = request.user, 
            title=data['title'],
            deadline=data['deadline'],
    # deadline = forms.DateTimeField()
            description = data['description'],
        )
        task.tags.add(*data['tags'].split(','))
        task.save()
        return redirect(task)

    return render(request, 'coreApp/edit/task-add.html', context)

@csrf_protect
@login_required
def squad_ditail(request, pk):
    squad = get_object_or_404(Squad, pk=pk)
    
    boards_list = []
    for board_slug, board_name in Task.STATUS_LIST:
        boards_list.append([
            board_slug,
            board_name,
            squad.tasks.filter(status=board_slug)
        ])
    

    context= {
        'squad':squad,
        'boards_list':boards_list,
    }   

    if request.method == "POST":
        data = request.POST
        print()
        

        if 'event' in data:
            task = Task.objects.get(pk=int(data['task_pk']))
            if data['event'] == 'change_status':
                task.status = data['target_pk']
                task.save()

            if data['event'] == 'get_task_info':
                response= {
                    'title':str(task),
                    'pk':str(task.pk),
                    'description':task.description,
                    'url':str(task.get_absolute_url()),
                    # 'is_normal':str(bnode.is_normal),
                    # 'weight':str(bnode.weight)
                    }
                return JsonResponse(response)
    return render(request, 'coreApp/squad-ditail.html', context)

@login_required
# @csrf_protect # - for POST
def task_ditail(request, pk):
    
    task = get_object_or_404(Task, pk=pk)
    
    context= {
        'task': task,
        'available':task.is_available(request.user)
    }   

    if request.method == "POST":
        data = dict(request.POST)
        print(data)

    return render(request, 'coreApp/task-ditail.html', context)

@login_required
def task_edit(request, pk):
    task = get_object_or_404(Task, pk=pk)

    if request.user != task.author:
        return HttpResponseNotFound()

    context = dict()
    context['form'] = MainTaskForm(initial={ 
        'title': task.title,
        'deadline': task.deadline,
        'description': task.description
    })
    context['tags'] = task.tags_list
    context['tag_list'] = Tag.objects.all()

    if request.method == "POST":
        data = request.POST
        print(dict(data))
        if 'event' in data:
            if data['event'] == 'del_task':
                task.delete()
                return redirect(reverse("user_home"))
        context['form'] = MainTaskForm(data)

        # # data validate

        task.author = request.user 
        task.title=data['title']
        task.deadline=data['deadline']
    # deadline = forms.DateTimeField()
        task.description = data['description']
        task.tags.clear()
        task.tags.add(*data['tags'].split(','))
        task.save()
        return redirect(task)

    return render(request, 'coreApp/edit/task-edit.html', context)