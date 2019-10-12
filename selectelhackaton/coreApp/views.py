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

@login_required
def add_task(request):

    if request.method == "POST":
        data = request.POST

        # data validate

        task = Task.objects.create(
            
        )
        task.save()
        return redirect(task)

    return render(request, 'coreApp/order-ditail.html', context)

@login_required
# @csrf_protect # - for POST
def task_ditail(request, pk):
    order = get_object_or_404(Task, pk=pk)

    context= {
        'order': order
    }

    if request.method == "POST":
        data = dict(request.POST)
        print(data)

    return render(request, 'coreApp/order-ditail.html', context)