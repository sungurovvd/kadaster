# kadaster
---
###
Проект - тестовое задание, выполненное с использованием фреймворка Django.
## Инструкции по запуску
 - Клонируйте репозиторий
   
 - Запустите контейнер с БД Postgres следующей командой:  
 > docker-compose up 
 - Создайте миграцию:
> docker-compose run web python manage.py makemigrations  
 - Примените миграции:
> docker-compose run web python manage.py migrate
 - Создайте пользователя:
> docker-compose run web python manage.py createsuperuser 
 - Задайте юзернейм и пароль.


---
## Примеры запросов
- Запрос существования требуемого кадастрового номера с заданной шириной и долготой:
>http://localhost:8000/query/

Пример отправляемого JSON:
> {
  "cadastre_number": 1,
  "latitude": 1,
  "longitude": 1
}

- Запрос на результат ответа, запрашиваемого раннее кадастрового номера:
>http://localhost:8000/result/
 
Пример отправляемого JSON:
> {
  "cadastre_number": "1"
}

-Запрос истории отправляемых запросов:
>http://localhost:8000/history/

-Проверка соединения:
>http://localhost:8000/ping/

 
