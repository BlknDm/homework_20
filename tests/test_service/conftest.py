from unittest.mock import MagicMock

import pytest

from dao.director import DirectorDAO
from dao.genre import GenreDAO
from dao.model.director import Director
from dao.model.genre import Genre
from dao.model.movie import Movie
from dao.movie import MovieDAO
from setup_db import db


@pytest.fixture()
def director_dao():
    director_dao = DirectorDAO(db.session)

    mike = Director(id=1, name='mike')
    poly = Director(id=2, name='poly')
    sam = Director(id=3, name='sam')

    director_dao.get_one = MagicMock(return_value=mike)
    director_dao.get_all = MagicMock(return_value=[mike, poly, sam])
    director_dao.create = MagicMock(return_value=Director(id=3))
    director_dao.update = MagicMock()
    director_dao.delete = MagicMock()

    return director_dao


@pytest.fixture()
def genre_dao():
    genre_dao = GenreDAO(db.session)

    horror = Genre(id=1, name='horror')
    comedy = Genre(id=2, name='comedy')
    drama = Genre(id=3, name='drama')

    genre_dao.get_one = MagicMock(return_value=horror)
    genre_dao.get_all = MagicMock(return_value=[horror, comedy, drama])
    genre_dao.create = MagicMock(return_value=Genre(id=3))
    genre_dao.update = MagicMock()
    genre_dao.delete = MagicMock()

    return genre_dao


@pytest.fixture()
def movie_dao():
    movie_dao = MovieDAO(db.session)

    sky = Movie(id=1, title='sky', year=2020)
    pro = Movie(id=2, title='pro', year=2021)
    best = Movie(id=3, title='best', year=2022)

    movie_dao.get_one = MagicMock(return_value=sky)
    movie_dao.get_all = MagicMock(return_value=[sky, pro, best])
    movie_dao.create = MagicMock(return_value=Movie(id=3))
    movie_dao.update = MagicMock()
    movie_dao.delete = MagicMock()

    return movie_dao
