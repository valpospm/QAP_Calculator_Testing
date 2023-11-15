import pytest

from app.calc import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,5, 6) == 11

    def test_multiply_success(self):
        assert self.calc.multiply(self, 10, 2) == 20

    def test_division_success(self):
        assert self.calc.division(self, 60, 3) == 20

    def test_subtraction_success(self):
        assert self.calc.subtraction(self, 650, 49) == 601

    def teardown(self):
        print('Выполнение метода Teardown')
