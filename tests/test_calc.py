import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        '''Проводим инициализацию приложения калькулятор'''
        self.calc = Calculator

    def test_adding_success(self):
        '''Проводим позитивный тест на сложение'''
        assert self.calc.adding(self,5, 6) == 11

    def test_multiply_success(self):
        '''Проводим позитивный тест на умножение'''
        assert self.calc.multiply(self, 10, 2) == 20

    def test_division_success(self):
        '''Проводим позитивный тест на деление'''
        assert self.calc.division(self, 60, 3) == 20

    def test_subtraction_success(self):
        '''Проводим позитивный тест на вычетание'''
        assert self.calc.subtraction(self, 650, 49) == 601

    def teardown(self):
        '''Реализуем метод Teardown для освобождения внешних ресурсов'''
        print('Выполнение метода Teardown')
