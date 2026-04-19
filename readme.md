# Автоматизация тестирования kaspersky.ru

Проект содержит **набор автоматизированных тестов** для проверки функциональности сайта [kaspersky.ru](https://www.kaspersky.ru).  
Тесты написаны на **Python** с использованием **Selenium WebDriver**, **Pytest**, **Allure Reports**.  
Поддерживается **локальный запуск**, **удалённый запуск через Selenoid**, а также **параметризованная сборка в Jenkins**.

---

## :page_facing_up: Содержание

1. [Что тестируется](#что-тестируется)
2. [Технологии и инструменты](#технологии-и-инструменты)
3. [Запуск тестов](#запуск-тестов)
   - [Локальный запуск](#локальный-запуск)
   - [Запуск через Selenoid](#запуск-через-selenoid)
   - [Параметры командной строки](#параметры-командной-строки)
4. [Allure Reports](#allure-reports)
5. [Примеры запуска](#примеры-запуска)
6. [Скриншоты](#cкриншоты)

---

## :test_tube: Что тестируется

| Тест | Описание |
|------|----------|
| `test_1_homepage_title` | Проверка заголовка главной страницы |
| `test_2_services_navigation` | Навигация к разделу «Для бизнеса» и переход на страницу продуктов |
| `test_3_product_cards_presence` | Присутствие карточек продуктов (Максимальная, Оптимальная, Базовая защита) |
| `test_4_product_card_details` | Клик по кнопке «Купить», переход в форму оформления, проверка текста «1. Укажите ваши данные» |
| `test_5_search_functionality` | Поиск по слову «антивирус», проверка результатов |
| `test_6_contact_form` | Заполнение формы «Заказать расследование» (10+ полей, выпадающие списки со скроллом, чекбокс, отправка) и проверка появления капчи |

---

## :hammer_and_wrench: Технологии

<p allign="left">
<img allign="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" height="40" width="40" />
<img allign="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" height="40" width="40" />
<img allign="center" src="ttps://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-plain-wordmark.svg" height="40" width="40" />
<img allign="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-line.svg" height="40" width="40" />
              
        
---

## :arrow_forward: Запуск тестов

### Локальный запуск (Chrome, без Selenoid)

`pytest tests/ --remote_url="" --alluredir=allure-results`

### Запуск через Selenoid

`pytest tests/ pytest tests/ --remote_url=https://selenoid.autotests.cloud/wd/hub --browser=chrome --browser_version=128.0`

### Запуск с другими браузерами

`pytest tests/ --browser=firefox --remote_url=https://selenoid.autotests.cloud/wd/hub`

### Запуск с headless-режимом и изменённым разрешением

`pytest tests/ --headless --window_width=1366 --window_height=768`

### Запуск конкретного теста

`pytest tests/test_6_contact_form.py -v`

---

## :bar_chart: Allure Reports
### Генерация отчёта
После прогона тестов с ключом `--alluredir=allure-results` выполните:

`allure serve allure-results`   
Отчёт откроется в браузере автоматически и будет содержать:

- Шаги тестов (с вложенными шагами)
- Скриншоты после каждого теста
- Скриншоты при падении (дополнительно)
- Логи консоли браузера
- Видеозапись (при запуске через Selenoid)
- HTML-код страницы (при падении)
- уведомлене на бота telegram 

---

## :pushpin: Примеры запуска

### Пример 1: Локальный прогон всех тестов с отчётом

`pytest tests/ --remote_url="" --alluredir=allure-results`  
`allure serve allure-results`

### Пример 2: Только тест «проверка сервиса» через Selenoid (Firefox, headless)

`pytest tests/test_2_services_navigation.py -v --selenoid_url=https://selenoid.autotests.cloud/wd/hub --browser=firefox --browser_version=125.0 --headless=true`


### Пример 3: Запуск в Jenkins с кастомными параметрами
При запуске сборки в Jenkins выберите:

`BROWSER = firefox`   
`WINDOW_WIDTH = 1366`   
`WINDOW_HEIGHT = 768`   
`HEADLESS = true`

#### Jenkins выполнит команду:

`pytest tests/ --browser=edge --window_width=1366 --window_height=768 --headless --alluredir=allure-results`

## :ticket:Cкриншоты

<img src="resources/allure report task15.JPG" width="600">
<img src="resources/telegram report.JPG" width="600">