from pages.api import API

import allure

api = API("https://api.kinopoisk.dev/v1.4/")

headers = {
    "accept": "application/json",
    "X-API-KEY": "MCR638D-DJK4YEV-GX2R3QC-VW7MPYT"
}


@allure.title("Поиск фильмов по наименованию")
@allure.description("Отправка запросы, где указывается название фильма, а также headers, где указывается токен и в каком формате представляют собой данные. Проверяется статус код и совпадение по альтернативному имени фильма.")
@allure.severity(allure.severity_level.CRITICAL)
def test_movies_by_name():
    movies = api.get_movies_by_name('Interstellar', headers)
    data = movies.json()
    movie_data = data['docs'][0]
    movie_name = movie_data['alternativeName']
    assert movies.status_code == 200
    assert movie_name == 'Interstellar'


@allure.title("Поиск сериалов по наименованию")
@allure.description("Находим фильм по названию с указанием headers, где указывается токен и в каком формате представляют собой данные. Проверка на статус успешного запроса.")
@allure.severity(allure.severity_level.CRITICAL)
def test_serial_by_name():
    movies = api.get_serial_by_name('Game of Thrones', headers)
    data = movies.json()
    movie_data = data['docs'][0]
    movie_name = movie_data['alternativeName']
    assert movies.status_code == 200
    assert movie_name == 'Game of Thrones'


@allure.title("Поиск фильма с указание id")
@allure.description("Находим фильм по id с указанием headers, где указывается токен и в каком формате представляют собой данные. Проверка на статус успешного запроса.")
@allure.severity(allure.severity_level.NORMAL)
def test_movie_id():
    movie = api.get_find_movie_id('12362', headers)
    movie.json()
    assert movie.status_code == 200


@allure.title("Поиск актеров")
@allure.description("Поиск актеров по имени, также можно указать фамилию. Проверка успешного запроса и совпадения по поиску.")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_actor():
    actor = api.get_list_actor('Ben Affleck', headers)
    data = actor.json()
    actor_data = data['docs'][0]
    actor_name = actor_data['enName']
    assert actor.status_code == 200
    assert actor_name == 'Ben Affleck'

@allure.title("Поиск режиссера")
@allure.description("Поиск режиссера по имени, также можно указать фамилию. Проверка успешного запроса и совпадения по поиску.")
@allure.severity(allure.severity_level.CRITICAL)
def test_find_actor():
    actor = api.get_list_actor('Steven Spielberg', headers)
    data = actor.json()
    actor_data = data['docs'][0]
    actor_name = actor_data['enName']
    assert actor.status_code == 200
    assert actor_name == 'Steven Spielberg'