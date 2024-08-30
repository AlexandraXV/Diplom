from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

import allure



class ui:

    def __init__(self, driver):
        self.driver = driver
        self.driver.get(
            "https://www.kinopoisk.ru/?from=tableau_yabro")
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()

    @allure.step('Закрывает всплывающее окно с рекламой.')
    def close_window(self):
        self.driver.find_element(
            By.CSS_SELECTOR, '.styles_closeIcon__Zvc5W').click()

    @allure.step("Найти фильм по наименованию {movie} через поисковик.")
    def find_movie(self, movie):
        self.driver.find_element(
            By.CSS_SELECTOR,
            '.styles_input__4vNAb.kinopoisk-header-search-form-input__input'
        ).send_keys(movie, Keys.ENTER)

    @allure.step("Ищет совпадение по наименованию фильма")
    def find_header_movie(self):
        return self.driver.find_element(By.XPATH, '//*[@id="block_left_pad"]/div/div[2]/div/div[2]/p/a').text

    @allure.step("Проверка функциональности кнопок во вкладке каналы.")
    def channels(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/nav/ul/li[5]/a'
        ).click()

        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[2]/button'
        ).click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[3]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[4]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[5]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[6]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[7]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[8]/button').click()
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/ul/li[9]/button').click()

    @allure.step("Ищет заголовок вкладки в телеканалах")
    def find_header_channels(self):
        return self.driver.find_element(By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div/div/div[1]/h1').text

    @allure.step("Возращение на главный экран через кнопку.")
    def back_in_main_screen(self):
        self.driver.find_element(
            By.XPATH, '//*[@id="__next"]/div[1]/div[2]/div[2]/div/div/div[1]/div/div/div/nav/ul/li[4]/a').click()
        self.driver.find_element(
            By.CSS_SELECTOR, '.styles_img__3hWmL.kinopoisk-header-logo__img').click()

    @allure.step("Ищет заголовок главной страницы")
    def find_main_header(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.styles_img__3hWmL.kinopoisk-header-logo__img').text

    @allure.step("Просмотр трейлера {value} через поисковик.")
    def watching_the_trailer(self, value):
        self.driver.find_element(
            By.CSS_SELECTOR,
            '.styles_input__4vNAb.kinopoisk-header-search-form-input__input'
        ).send_keys(value, Keys.ENTER)
        self.driver.find_element(
            By.XPATH, '//*[@id="block_left_pad"]/div/div[2]/div/div[1]/ul/li[2]/a').click()
        self.driver.find_element(By.XPATH, '//*[@id="tr_first_t61544"]/table[2]/tbody/tr[1]/td/table/tbody/tr/td/div/div/div').click()

    @allure.step("Поиск слова Трейлеры")
    def find_header_trailer(self):
        return self.driver.find_element(By.CSS_SELECTOR, '.breadcrumbs__link').text

    @allure.step("Поиск актера/режиссера {name} через  фильтр.")
    def filters(self, name):
        self.driver.find_element(
            By.CSS_SELECTOR, '.styles_advancedSearchIcon__Zxjax').click()
        self.driver.find_element(By.CSS_SELECTOR, '#find_people').send_keys(name)
        self.driver.find_element(
            By.CSS_SELECTOR, '.el_8.submit.nice_button').click()

    @allure.step("Поиск заголовка найденного человека")
    def find_header_filters(self):
        return self.driver.find_element(By.XPATH, '//*[@id="block_left_pad"]/div/div[2]/div/div[2]/p/a').text