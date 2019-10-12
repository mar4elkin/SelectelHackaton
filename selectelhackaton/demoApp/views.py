from django.views.generic.base      import TemplateView
from django.views.generic           import View
from django.shortcuts               import render, get_object_or_404
from django.template                import loader, RequestContext
from django.urls                    import reverse
from django.http                    import JsonResponse, HttpResponseNotFound, HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf   import csrf_protect
from django.utils.decorators        import method_decorator
from django.contrib.auth.decorators import login_required
from django.db.models               import Q
#from django.contrib.postgres.search import SearchVector


import                                     datetime   

@login_required
# @csrf_protect # - for POST
def order_ditail(request, pk):

    context= {
    }

    if request.method == "POST":
        data = dict(request.POST)
        print(data)

        if 'tags[]' in data:
            order.tags.add(*data['tags[]'])
            order.tags.add('adssads', 'asdsadas', '213213')

    return render(request, 'demoApp/order-ditail.html', context)