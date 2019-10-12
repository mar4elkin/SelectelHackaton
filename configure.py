#!/usr/bin/env python
import                                     django
from django.conf                    import settings
from django.core.management.utils   import get_random_secret_key
from django.template.loader         import get_template
from django.template                import engines

import                                     os
from datetime                       import datetime

from bullet.charDef                 import NEWLINE_KEY
from bullet                         import ( Bullet, SlidePrompt, Check, 
                                            keyhandler, styles, Input, 
                                            YesNo, Numbers )


BASE_DIR = os.path.dirname(os.path.dirname(__file__))

# TEMPLATES structure changed in Django 1.10
settings.configure(
    DEBUG=True,
    TEMPLATES=[dict(
        # DEBUG = True,
        BACKEND='django.template.backends.django.DjangoTemplates',
        APP_DIRS=True,
        DIRS=[
            os.path.join(BASE_DIR, 'config'),
        ],
    )],
)

try:
    django.setup()  # for Django >= 1.7
except AttributeError:
    pass  # must be < Django 1.7

commands_template = engines['django'].from_string("""
Выполните данные команды:

    python manage.py makemigrations selectelhackaton_auth demoApp
    python manage.py migrate
    python manage.py createsuperuser
    {% if facebook %}# Facebook
    python manage.py set_auth_provider facebook {{facebook.client_id}} {{facebook.secret}}{% endif %}
    {% if google %}# Google
    python manage.py set_auth_provider google {{google.client_id}} {{google.secret}}{% endif %}
    {% if github %}# GitHub
    python manage.py set_auth_provider github {{github.client_id}} {{github.secret}}{% endif %}
    {% if vk %}# VK
    python manage.py set_auth_provider vk {{vk.client_id}} {{vk.secret}}{% endif %}

Если у вас есть другие провайдеры, то вы можете добавить их подобным образом.
""")


class MinMaxCheck(Check):
    def __init__(self, min_selections=0, max_selections=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.min_selections = min_selections
        self.max_selections = max_selections
        if max_selections is None:
            self.max_selections = len(self.choices)

    @keyhandler.register(NEWLINE_KEY)
    def accept(self):
        if self.valid():
            return super().accept()

    def valid(self):
        return self.min_selections <= sum(1 for c in self.checked if c) <= self.max_selections

def heading(text):
    text = text.strip()
    line = '-' * len(text)
    print("\n%s\n%s\n%s\n" % (line, text, line))

def ask_provider(provider):
    if YesNo(f"Хотите ли вы сконфигурировать авторизацию через {provider}?\n"
              "(Для этого вам понадобяться Secret, Client ID)\n").launch():
        secret = Input(f"{provider} Secret: ").launch()
        client_id = Input(f"{provider} Client ID: ").launch()
        return dict(secret=secret, client_id=client_id)
    return dict(secret="secret", client_id="client_id")


def main():
    settings_template = get_template("settings.template.py")
    context = {
        'now': str(datetime.now()),
        'secret_key': get_random_secret_key(),
    }

    print('\n')
    print('(выбирать - Space; продолжить - Enter)')
    providers = MinMaxCheck(
                prompt = "Выбирите соц. приложения:",
                choices = [
                    'Facebook',
                    'Google',
                    'GitHub',
                    'VK'
                ],
                **styles.Exam
            ).launch()
    for provider in providers:
        context[provider.lower()] = ask_provider(provider)

    heading("Рендрим settings...")
    with open('config/settings.py', 'w') as out:
        out.write(settings_template.render(context, request=None))
    print("OK")

    heading("Дальше")
    print(commands_template.render(context, request=None))
    heading("Готово")

def iTitle(text, font="larry3d", color="blue"):
    try:
        import sys
        from colorama import init
        init(strip=not sys.stdout.isatty())
        from termcolor import cprint
        from pyfiglet import figlet_format
        
        cprint(figlet_format(text, font=font), color)

    except Exception as err:
        text = text.strip()
        line = '-' * len(text)
        print("\n%s\n%s\n%s\n" % (line, text, line))     

if __name__ == "__main__":
    iTitle("Django AllAuth RU", font="larry3d", color="green")
    main()