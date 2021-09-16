from flask import render_template
from config import app


class HomeController(object):

    @staticmethod
    @app.route('/')
    def index():
        """ Метод для загрузки шаблона главной страницы """
        return render_template('home/index.html')

    @staticmethod
    @app.route('/about')
    def about():
        """ Метод для загрузки шаблона страницы про сайт """
        return render_template('home/about.html')

    @staticmethod
    @app.route('/contact')
    def contact():
        """ Метод для загрузки шаблона страницы контактов """
        return render_template('home/contact.html')
