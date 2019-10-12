from allauth.socialaccount.models import SocialApp
from django.contrib.sites.models  import Site
from django.core.management.base  import BaseCommand


class Command(BaseCommand):
    help = 'Rename first or create new Site'

    def add_arguments(self, parser):
        parser.add_argument('name', type=str, help="Site display name")
        parser.add_argument('domain', type=str, help="Site Dimain")
        parser.add_argument('-c','--create',action='store_true', default=False, help="Create new Site")

    def handle(self, *args, **options):
        name = options['name']
        domain = options['domain']
        
        if options["create"]:
            s = Site(name=name, domain=domain,)
            s.save()
            self.stdout.write(self.style.SUCCESS(
            "Created site! name:'{}' \tdomain:'{}'".format(s.name, s.domain)
            ))
        else:
             # Delete the specific sites if it exists.
            Site.objects.filter(name=name).delete()
            s = Site.objects.first()
            s.name=name
            s.domain=domain
            s.save()
            self.stdout.write(self.style.SUCCESS(
            "Rename first site! name:'{}' \tdomain:'{}'".format(s.name, s.domain)
            ))
        