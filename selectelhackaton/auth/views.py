from django.contrib                 import messages
from django.contrib.auth.decorators import login_required
from django.urls                    import reverse_lazy
from django.views.generic.edit      import FormMixin, UpdateView
from django.template                import loader
from .forms                         import UserEditForm
from .models                        import User, UserProfile
from django.http                    import HttpResponse
class MyModelInstanceMixin(FormMixin):
    def get_model_instance(self):
        return None

    def get_form_kwargs(self):
        kwargs = super(MyModelInstanceMixin, self).get_form_kwargs()
        instance = self.get_model_instance()
        if instance:
            kwargs.update({'instance': instance})
        return instance


class UserEditView(UpdateView):
    """Allow view and update of basic user data.

    In practice this view edits a model, and that model is
    the User object itself, specifically the names that
    a user has.

    The key to updating an existing model, as compared to creating
    a model (i.e. adding a new row to a database) by using the
    Django generic view ``UpdateView``, specifically the
    ``get_object`` method.
    """
    form_class = UserEditForm
    template_name = "allauth/account/profile_edit.html"
    view_name = 'account_edit_profile'
    success_url = reverse_lazy(view_name)

    def get_object(self):
        return self.request.user

    def form_valid(self, form):
        form.save()
        messages.add_message(self.request, messages.INFO, 'User profile updated')
        return super(UserEditView, self).form_valid(form)


account_edit_profile = login_required(UserEditView.as_view())

@login_required
def member_profile(request, pk):
    t = loader.get_template('allauth/account/profile.html')
    c = {'user1': User.objects.get(pk=pk)}  #{'foo': 'bar'}
    return HttpResponse(t.render(c, request), content_type='text/html')