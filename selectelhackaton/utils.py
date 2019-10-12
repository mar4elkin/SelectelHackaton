from django.http                    import HttpResponse, HttpResponseRedirect
from django.template                import loader, RequestContext
from django.shortcuts               import render, get_object_or_404
from django.views.generic           import View
 
class SimpleAuthMixinView(View):
    template_name = None
    context = None

    
    def get(self,request):
        t = loader.get_template(self.template_name)
        if self.context:
            self.context = {}
        return HttpResponse(t.render(self.context, request), content_type='text/html')


# model_obj.__name__.lower()