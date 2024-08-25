# Укорачиватель ссылок 
Сайт, для того чтобы сократить ссылку и сделать ее более красивой :)
# Описание
Сайт Укорачиватель ссылок созданный с использованием микрофреймворка Flask в рамках обучения по программе Python Pro
## Технологии
* Python
* Flask
* WTForms
* SQLAlchemy
## Как запустить
1. Склонируйте репозиторий
2. Создайте и активируйте виртуальное окружение
```commandline
python -m venv venv
source venc/Scripts/activate
```
3. Установите зависимости
```commandline
pip install -r requirements.txt
```
4. Создайте файл .env и укажите настройки подключения к БД и другие параметры
```commandline
DATABASE_URI=sqlite:///urls.db
SECRET_KEY=YOUR_SECRET_KEY
```
5. Запустите Flask приложение
```commandline
flask run
```