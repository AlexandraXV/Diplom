from ui import ui

from time import sleep

from selenium import webdriver


import allure

driver = webdriver.Chrome()
ui_page = ui(driver)


@allure.title("Поиск фильма")
@allure.description("Поиск фильма через поиск по селектору, нажатие на кнопку через Keys")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_movie():
    ui_page.find_movie("The Crow")


@allure.title("Кнопка Телеканалы")
@allure.description("Тестирование кнопки Телеканалы. Проверка функциональности кнопок внутри вкладки.")
@allure.severity(allure.severity_level.CRITICAL)
def test_channels():
    ui_page.channels()


@allure.title("Возрат на главную страницу")
@allure.description("Переход на вкладку, нажатие на кнопку Кинопоиск для возврата на главную страницу.")
@allure.severity(allure.severity_level.CRITICAL)
def test_back_main():
    ui_page.back_in_main_screen()


@allure.title("Просмотр трейлера")
@allure.description("Поиск фильма через поисковик, нажатие на кнопку Трейлер.")
@allure.severity(allure.severity_level.CRITICAL)
def test_watching_the_trailer():
    ui_page.watching_the_trailer('The Avengers')


@allure.title("Использвание фильтра")
@allure.description("Поиск актера/режиссера по имени, также можно указать фамилию.")
@allure.severity(allure.severity_level.CRITICAL)
def test_filters():
    ui_page.filters('Steven Spielberg')
