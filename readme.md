## Быстрый старт

### Требования:
    1) Python версии 3.10 или выше
    2) Поднятый Selenium Server (если его нет, то в папке SeleniumGreed есть инструкция как поднять локально)
    3) Allure Framework (интсрукция по установке https://docs.qameta.io/allure/)

### Быстрый старт (Windows):
    1) Установите пакеты из requirements.txt:
        python -m pip install --upgrade pip
        pip install -r requirements.txt
    2) Запустите тесты командой (при необходимости каталог хранения результатов можно изменить): 
        pytest --alluredir=./allure-results .\UI\Tests\
    3) После окончания тестов посмотрите отчет командой:
        allure serve {путь до папки проекта}\TestTaskSimbirSoft\allure-results\