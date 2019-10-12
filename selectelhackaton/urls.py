from django.urls             import path, include, re_path
from django.contrib          import admin
from django.views.generic    import TemplateView
from django.conf.urls.static import static
from django.conf             import settings

from .auth.views import account_edit_profile, member_profile
from .views import MemberIndex

urlpatterns = [
    # Landing page area
    re_path(r'^$', TemplateView.as_view(template_name='visitor/landing-index.html'), name='landing_index'),
    path('about', TemplateView.as_view(template_name='visitor/landing-about.html'), name='landing_about'),
    path('contact', TemplateView.as_view(template_name='visitor/contact.html'), name='website_contact'),
    
    # Account management is done by allauth
    path('accounts/', include('allauth.urls')),

    # Account profile and member info done locally
    path('accounts/profile/edit', account_edit_profile, name='account_edit_profile'),
    path('member/', MemberIndex.as_view(), name='user_home'),
    path('accounts/profile/<int:pk>/', member_profile, name='member_profile'),

    # demoApp
    path('demo/', include('selectelhackaton.demoApp.urls')), 

    # demoApp
    path('core/', include('selectelhackaton.coreApp.urls')), 

    # Usual Django admin
    path('admin/', admin.site.urls),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
