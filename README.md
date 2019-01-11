# Обрезка ссылок с помощью Битли
Скрипт помогает укоротить ссылку или посмотреть статистику по короткой ссылке.

### Как установить
Для использования скрипта необходимо:
1. зарегистрироваться на сайте [bitly.com](https://bitly.com).
2. получить API токен.
3. создать файл '.env' и записать там полученный токен:
```
TOKEN=ваш_токен
```

Python3 должен быть уже установлен. 
Затем используйте pip (или pip3, есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Рекомендуется использовать virtualenv для изоляции проекта.

### Цель проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org).