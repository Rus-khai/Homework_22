# Данный проект создан для изучения Django
## Описание проекта
Этот проект создан для изучения Django. Он включает в себя следующие компоненты:
- **Homework_22**: Папка с проектом, в которой содержится код и файлы для выполнения домашних заданий.
- **config**: Папка с настройками Django, в которой содержится файл `urls.py`.
- **catalog**: Папка с моделями и представлениями для каталога, включая файлы `urls.py`, `views.py`, `forms.py`, и `models.py`.
- **blog**: Папка с моделями и представлениями для блога, включая файлы `urls.py`, `views.py`, `forms.py`, и `models.py`.
- **static**: Папка с статическим содержимым, включая файлы `css` и `js`.
- **users**: Папка с моделями и представлениями для пользователей, включая файлы `urls.py`, `views.py`, `forms.py`, и `models.py`.
- **media**: Папка с медиа-файлами, включая файлы `blog` и `media`.
## Требования
- Python 3.14
- Django 6.0
## Установка
1. Создайте виртуальное окружение:
   ```bash
   python -m venv /Users/ruslan/PycharmProjects/Homework_22/.venv
   ```
2. Активируйте виртуальное окружение:
   ```bash
   source /Users/ruslan/PycharmProjects/Homework_22/.venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
   ## Запуск проекта
1. Создайте базу данных:
   ```bash
   python manage.py migrate
   ```
2. Создайте суперпользователя:
   ```bash
   python manage.py createsuperuser
   ```
   3. Запустите сервер:
      ```bash
      python manage.py runserver
      ```
