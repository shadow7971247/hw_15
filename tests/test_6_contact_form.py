import allure
from pages.contact_investigation_page import ContactInvestigationPage
from models.contact_form import ContactFormData


@allure.feature("Форма обратной связи")
@allure.story("Запрос на расследование")
@allure.title("После заполнения формы и нажатия Отправить появляется капча")
def test_captcha_appears_after_form_submission(driver):
    form_data = ContactFormData(
        name="Jane Doe",
        email="info@example.com",
        phone="+71234567890",
        country="Монголия",
        company_name="тикток для бедных",
        employees_count="1",
        help_required="Восстановление данных",
        incident_type="Уязвимость",
        incident_details="тест заполнения формы"
    )

    page = ContactInvestigationPage(driver)

    with allure.step("Открыть страницу с формой"):
        page.open()

    with allure.step("Заполнить все поля формы"):
        page.fill_form(form_data)

    with allure.step("Нажать кнопку Отправить"):
        page.submit()

    with allure.step("Проверить, что появилась капча"):
        page.captcha_should_appear()