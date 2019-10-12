# demo-allauth-bootstrap-ru

Это шаблон для Web приложений с авторизацией и Bootstrap4.

Как именно получить токены лучше гуглить самим

# Установка:
Не забудьте про:

0. (опционально) Для красивого вывода и управления
        
        $ pip install -r optional_requirements.txt

Если у вас Ubuntu или Debain, то может понадобиться установить:

        $ sudo apt-get install libpq-dev python3-dev python-dev

1. Начало:

        $ pip install -r requirements.txt
        $ python configure.py

2. Подготовка:

        $ python manage.py makemigrations selectelhackaton_auth demoApp

3. Миграция:

        $ python manage.py migrate

4. Создание Суперпользователя:

        $ python manage.py createsuperuser

5. Изменяет внутренней адрес сайта:

        python manage.py rename_site Dev 127.0.0.1:8000

6. Добавляем social providers (en):

   Run this for each provider you want to include.
   
        $ python manage.py set_auth_provider google GOOGLE_CLIENT_ID GOOGLE_SECRET_ID
        saved: Google (...)
        
        $ python manage.py set_auth_provider facebook FACEBOOK_CLIENT_ID FACEBOOK_SECRET_ID
        saved: Facebook (...)

   This essentially runs SQL like:
   
        DELETE FROM socialaccount_socialapp WHERE provider='google';
        INSERT INTO socialaccount_socialapp (provider, name, secret, client_id, `key`)
        VALUES ("google", "Google", "SECRET", "CLIENT", '');
        INSERT INTO socialaccount_socialapp_sites (socialapp_id, site_id) VALUES (
          (SELECT id FROM socialaccount_socialapp WHERE provider='google'),1);
        
7. Старт!:

        $ python manage.py runserver

   Load the site at http://127.0.0.1:8000

   You should see a landing page. Click "Join" or "Login".

# Рекомендации по тестированию проекта
Запустить все тесты:
        $ ./manage.py test

В  ProjectName/tests.py класс AllViewsTestCase парсит URL из всех файлов urls.py, можно там подсмотреть кое-что и для себя, или можете доработать.

Для проета рекомендую сдеующую структуру для тестов:

demoApp/
* tests/
  * \_\_init\_\_.py
  * test_models.py # для тестирования моделей
  * test_views.py # для тестирования views

# Старт для ПРО

1. Зарускаем:
        
        bash rename_project.sh
        
2. Начинаем новую историю:

        git init

3. И ещё не забудьте текущий адрес:

        python manage.py rename_site Release mydomain.com -cs

## Для продвинутых ПРО
1. Переименовать selectelhackaton в projectname, а SelectelHackaton в ProjectName
2. Переименовать дирректорию selectelhackaton в projectname
3. Изменить contact.html
4. Удалить demo
5. При необходимости изменить .gitignore
6. Удаляем git

        rm -rf .git/

7. Удаляем ненужное:

        rm LICENSE README.md confif/settings.template.py configure.py
8. Начинаем новую историю:

        git init

9. SQLite - это круто, но не для реального проекта!
10. И ещё не забудьте про:

        python manage.py rename_site Release mydomain.com -cs

## Визуализация моделий:
Install diagrams generators
```
pip install pydotplus
```
Generate diagrams
```
$ python manage.py graph_models -a -o myapp_models.png
$ ./manage.py demoApp selectelhackaton -g -o ../img/my_project_visualized.png
```

### Про Facebook Login (en)

Follow these instructions if you want to use Facebook as an authentication provider.
Skip otherwise.

Sarah describes this nicely in [her article][2]

Aside from UI changes, the method she described worked well.

1. Go to [facebook-developer-settings].

2. Add app

3. Create a test app (under the above app)

4. Go to Settings > Advanced

5. Do *not* add any server to Server IP Whitelist ([facebook-whitelist-ip-error])

6. Add product "Facebook Login"

7. Enable if not automatically selected: Client OAuth Login, Web OAuth Login

8. Add OAuth redirect URL (in any order):
  ``http://127.0.0.1:8000/``
  ``http://127.0.0.1:8000/accounts/facebook/``
  ``http://127.0.0.1:8000/accounts/facebook/login/callback/``

  Note: If you're loading your site with ``localhost:8000`` you should use "http://localhost:8000/..." 
  above. Whichever you choose, do it consistently and you should be ok.

Note: The "app secret" and "client id" are a bit confusing with Facebook.  
You want to record the "Facebook App Secret" and the "Facebook App ID". The latter
"Facebook App ID" becomes the "client ID" from a Django Allauth perspective.


### Configure Google Login

Follow these instructions if you want to use Google as an authentication provider.
Skip this section otherwise.

To set up Google, follow the [Google oauth instructions][3] or [this help answer][4]
which is basically:


1. Go to https://console.developers.google.com/

2. Create a new app

3. Make sure that app is selected (next to the "Google APIs" Logo in the top-left)

4. In the left navigation rail under "APIs and Services", click "Credentials"

5. Create new oauth client ID

   You will need to specify some "consent screen details". You can skip most
   of the fields. 

6. For Authorized Javascript Origins, add: http://127.0.0.1:8000

7. For Authorized Redirect URIs, add: http://127.0.0.1:8000/accounts/google/login/callback/

8. Click "Create"

9. Copy the "client ID" and "client secret" strings and keep each handy - you'll need them shortly.


Reminder: if you're loading your site at ``localhost:8000`` then you'll need to set the
URIs above to ``http://localhost:8000/..." etc. I recommend not doing that. Instead, just
load your local site as http://127.0.0.1:8000/



# Установка с помошью Docker:
        
        $ docker-compose up -d --build
        $ docker exec -ti selectelhackaton_django python manage.py makemigrations allauthdemo_auth demoApp
        $ docker exec -ti selectelhackaton_django python manage.py migrate
        $ docker exec -ti selectelhackaton_django python manage.py createsuperuser
        $ docker exec -ti selectelhackaton_django python manage.py collectstatic