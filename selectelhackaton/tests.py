from django.test                import TestCase
from django.test                import Client
from django.urls                import reverse
from django.conf                import settings
import                                 importlib
import                                 django
from inspect                    import signature as sig

from selectelhackaton.auth.models    import User, UserProfile
from selectelhackaton.urls           import urlpatterns

class AllViewsTestCase(TestCase):
    global_url_patterns = [] 
    url_pattern_modules = [] # ссылки на другие urls.py

    def updateUrlPattern(self):
        for urlpattern in urlpatterns:
            if issubclass(type(urlpattern), django.urls.resolvers.URLPattern):
                self.global_url_patterns.append(urlpattern)
            elif issubclass(type(urlpattern), django.urls.resolvers.URLResolver):
                self.url_pattern_modules.append(urlpattern)

    def get_arg_from_URLPattern(self, urlpattern):
        return [str(p) for p in sig(urlpattern.callback).parameters.values()]

    def URLPattern_has_args(self, urlpattern):
        return self.get_arg_from_URLPattern(urlpattern) != ['self', 'request', '*args', '**kwargs']

    def setUp(self): 
        """Установки запускаются перед каждым тестом."""
        user = User.objects.create(email='testuser')
        user.set_password('12345')
        user.save()

        self.c = Client()
        self.c.force_login(user)

        self.updateUrlPattern()

        
        
    # TESTS: 
    def test_simple_view(self): # static/
        url_pattern = self.global_url_patterns[-1]
       # print("*** ", url_pattern)
        self.assertTrue(self.URLPattern_has_args(url_pattern))

    def test_login_in_tests(self):
        response = self.c.get(reverse("user_home"))
        
        # Check that the response is 200 OK.
        print(response)
        self.assertEqual(response.status_code, 200)

    def test_global_views(self):
        for i in  self.global_url_patterns:
            if not self.URLPattern_has_args(i):
                print('***\t Check:', i)
                response = self.c.get(reverse(i.name))
                # Check that the response is 200 OK.
                self.assertEqual(response.status_code, 200)

