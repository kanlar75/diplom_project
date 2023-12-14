Данная работа представляет собой backend-часть для сайта объявлений. 

Frontend-часть уже готова.
Frontend проекта реализован на React (папка frontend_react) и предоставлен в готовом виде.
Backend реализован на Python c использованием Django Rest_Framework и JWT.

В Backend-части проекта реализован следующий функционал:

- Авторизация и аутентификация пользователей.
- Распределение ролей между пользователями (пользователь и админ).
- CRUD для объявлений на сайте (админ может удалять или редактировать все объявления, 
а пользователи только свои).
- Под каждым объявлением пользователи могут оставлять отзывы.
- В заголовке сайта можно осуществлять поиск объявлений по названию.

Также реализована пагинация для эндпоинта /ads/ 4 объекта на странице (ограничение фронта).

Анонимный пользователь может:
- получать список объявлений.

Пользователь может:

- получать список объявлений,
- получать одно объявление,
- создавать объявление
- редактировать и удалять свое объявление,
- получать список комментариев,
- создавать комментарии,
- редактировать/удалять свои комментарии.

Администратор может:

Дополнительно к правам пользователя редактировать или удалять
объявления и комментарии любых других пользователей.

Реализованы все эндпоинты согласно документации frontend.

Тестирование выполнялось в Unitest. Покрытие тестами 92%.
Для запуска тестов с расчетом покрытия выполните команду: 
coverage run manage.py test 
coverage report

Документация доступна по адресам: 
http://127.0.0.1:8000/api/redoc-tasks/ # Frontend
http://127.0.0.1:8000/api/redoc/ # Бэкэнд 
http://127.0.0.1:8000/api/swagger/ # Swagger

ЗАПУСК ПРОЕКТА ЛОКАЛЬНО.

Клонируйте проект. Активируйте виртуальное окружение. 
Установите зависимости.

Создайте Базу данных PostgreSQL командами:
1. psql -U <имя пользователя>
2. CREATE DATABASE <имя базы данных>;
3. \q 

Пропишите переменные окружения в файл .env. 
Используемые в проекте переменные окружения записаны в файле .env.sample.
Для локального запуска установите ENV_TYPE='local'

Для миграции в базу данных используйте команду: python manage.py migrate

Для первичного заполнения базы данных объявлениями, комментариями и пользователями из фикстур:
python manage.py loadall.
Или для создания только суперпользователя и пользователей используйте команду: 
python manage.py create_users

Выполните команду: python manage.py runserver

В адресной стоке браузера введите адрес http://127.0.0.1:8000/api/admin
Пароль и логин для суперпользователя:
login: admin@test.com password: 111

Для всех пользователей (user1@test.com, user2@test.com, user3@test.com, user4@test.com) password: 111.


ЗАПУСК ПРОЕКТА В DOCKER.

Клонируйте проект.
Установите docker и при необходимости docker-compose.
Пропишите переменные окружения в файл .env. 

Создайте образ командой:
docker-compose build

Используемые в проекте переменные окружения записаны в файле .env.sample.
Для запуска в docker установите ENV_TYPE='docker'

Запустите контейнеры командой:
docker-compose up

В адресной стоке браузера введите адрес http://127.0.0.1:8000/api/admin
Пароль и логин для суперпользователя:
login: admin@test.com password: 111

Первоначальное заполнение базы данных выполняется из фикстур.
Для всех пользователей (user1@test.com, user2@test.com, user3@test.com, user4@test.com) password: 111.


Если у вас возникли вопросы или проблемы при использовании проекта, 
свяжитесь со мной по электронной почте kls75@yandex.ru или оставьте комментарий.
