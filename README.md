# Editorial-Hub
[Проект розгорнутий на цьому сайті](https://google.com/)

## 📝 Опис проекту
Editorial-Hub - це веб-платформа для управління новинним контентом, розроблена на Django. Система дозволяє редакторам керувати новинним контентом та забезпечує зручний інтерфейс для читачів.
#

## 🚀 Функціональність
- Система автентифікації та авторизації редакторів
- Управління профілями редакторів з можливістю завантаження фото
- Створення та редагування новин
- Адаптивний користувацький інтерфейс
- Автоматична обробка зображень профілю

## 💻 Технології
### Backend
- Python 3.x
- Django 5.1.3
- django-crispy-forms
- django-bootstrap4
- django-resized
- Pillow

### Frontend
- Bootstrap 4
- jQuery
- Modernizr
- Salvattore
- Waypoints

## 📁 Структура проекту

Editorial-Hub/
├── accounts/ # Додаток для управління користувачами
├── news/ # Додаток для управління новинами
├── templates/ # HTML шаблони
│ ├── news/
│ └── registration/
├── static/ # Статичні файли
│ ├── css/
│ └── js/
├── media/ # Медіа файли
│ ├── news_images/
│ └── profile_images/
└── tests/ # Тести проекту

## 📄 Інструкція для розгортання
### 1. Клонування репозиторію:
```bash
git clone https://github.com/yourusername/Editorial-Hub.git
```
### 2. Створення віртуального середовища:
```
python -m venv venv
```
### 3. Активація віртуального середовища:
#### Windows
```bash
venv\Scripts\activate
```
#### Linux or MacOS
```bash
source venv/bin/activate
```
### 4. Встановлення залежностей:

```bash
pip install -r requirements.txt
```
### 5. Виконання міграцій:
```bash
python manage.py migrate
```
### 6. Запуск сервера:
```bash
python manage.py runserver
```
## Тестування 🧪
Проект має повне покриття тестами для:
- В'юшок (views)
- Форм (forms)
- Моделей (models)
- Пошукової функціональності

Для запуску тестів використовуйте:
```bash
python manage.py test tests/
```
## 📄 Тестовий користувач
```
username: test
password: 1234tesT
```

## 🎇 Скріншоти
![alt text](<Screenshot 2024-12-05 214407.png>)
![alt text](<Screenshot 2024-12-05 214416.png>)
![alt text](<Screenshot 2024-12-06 002500.png>)
![alt text](<Screenshot 2024-12-06 001947.png>)
![alt text](<Screenshot 2024-12-06 002009.png>)