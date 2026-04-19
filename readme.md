# Автотесты для kaspersky.ru

Проект содержит набор автоматизированных тестов для проверки ключевых функций сайта [kaspersky.ru](https://www.kaspersky.ru).  
Тесты написаны на **Python** с использованием **Selenium WebDriver**, **Pytest**, **Allure Reports** и поддерживают запуск как локально, так и удалённо через **Selenoid**, а также интеграцию с **Jenkins**.

---

## 🚀 Основные возможности

- Проверка заголовка главной страницы
- Навигация к продуктам для бизнеса
- Присутствие карточек продуктов
- Детальная проверка карточки продукта (кнопки «Купить», переход в форму оформления)
- Функциональность поиска
- Заполнение сложной формы «Заказать расследование» с проверкой появления капчи
- Параметризация через командную строку (браузер, версия, headless, разрешение экрана)
- Генерация красивых отчётов Allure (скриншоты, логи, видео)
- Удалённый запуск в браузерах через Selenoid
- Параметризованная сборка в Jenkins с выбором параметров

---

## 🛠 Технологии

| Инструмент | Назначение
<p allign="left">
<img allign="center" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-plain-wordmark.svg" /> height="40" width="40" />
              
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/selenium/selenium-original.svg" />
                          

            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-plain-wordmark.svg" />
          
            <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jenkins/jenkins-line.svg" />
          
| Python 3.12+ | Язык программирования |
| Selenium WebDriver | Управление браузером |
| Pytest | Фреймворк для тестирования |
| Allure Reports | Генерация отчётов |
| Selenoid | Запуск тестов в контейнерах (Chrome, Firefox, Edge) |
| Jenkins | CI/CD (параметризованная сборка) |
| WebDriver Manager | Автоматическая загрузка локальных драйверов |
| python-dotenv | Управление секретами через .env |

---

## 📦 Установка и настройка

### 1. Клонирование репозитория

```bash
git clone https://github.com/shadow7971247/hw_15.git
cd hw_15