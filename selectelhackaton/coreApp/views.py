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
def add_task(request):
    context = dict()
    context['form'] = MainTaskForm()
    context['tag_name'] = Tag.objects.all()

    if request.method == "POST":
        data = request.POST
        context['form'] = MainTaskForm(data)



        print(dict(data))
        # # data validate

        task = Task.objects.create(
            author = request.user, 
            title=data['title'],
    # deadline = forms.DateTimeField()
            description = data['description'],
        )
        task.save()
        return redirect(task)

    return render(request, 'coreApp/edit/task-add.html', context)

@login_required
# @csrf_protect # - for POST
def task_ditail(request, pk):
    task = get_object_or_404(Task, pk=pk)

    context= {
        'task': task
    }

    if request.method == "POST":
        data = dict(request.POST)
        print(data)

    return render(request, 'coreApp/task-ditail.html', context)