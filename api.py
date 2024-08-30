import allure
import requests


class API:

    def __init__(self, url):
        self.url = url

    @allure.step("Поиск фильмов по названию: {value} с фильтрами.")
    def get_movies_by_name(self, value, headres):
        """
        Данный скрипт запрашивает страницу (page=),
        устанавливает лимит по кол-ву элементов на странице (limit=),
        также запрашивает название фильма (query=)
        """
        my_params = {
            'page': '1',
            'limit': '25',
            'query': value
        }
        resp = requests.get(
            self.url + 'movie/search', params=my_params, headers=headres)
        return resp

    @allure.step("Поиск серила по названию: {value} с фильтрами.")
    def get_serial_by_name(self, value, headres):
        """
        Данный скрипт запрашивает страницу (page=),
        устанавливает лимит по кол-ву элементов на странице (limit=),
        также запрашивает название фильма (query=)
        """
        my_params = {
            'page': '1',
            'limit': '25',
            'query': value
        }
        resp = requests.get(
            self.url + 'movie/search', params=my_params, headers=headres)
        return resp

    @allure.step("Поиск фильма по {id}")
    def get_find_movie_id(self, id, headers):
        resp = requests.get(self.url + 'movie/' + str(id), headers=headers)
        return resp

    @allure.step("Поиск актеров по имени: {name}")
    def get_list_actor(self, name, headers):
        my_params = {
            'page': '1',
            'limit': '25',
            'query': name
        }
        resp = requests.get(self.url + 'person/search',
                            params=my_params, headers=headers)
        return resp

    @allure.step("Поиск режиссеров по имени: {name}")
    def get_list_director(self, name, headers):
        my_params = {
            'page': '1',
            'limit': '25',
            'query': name
        }
        resp = requests.get(self.url + 'person/search',
                            params=my_params, headers=headers)
        return resp
