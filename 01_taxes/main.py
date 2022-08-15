class Property:
    """
    Базовый класс, описывающий имущество налогоплательщика.

    :args
        property_name(str): название имущества
        worth(int): стоимость имущества
    """
    def __init__(self, property_name, worth):
        self.__property_name = property_name
        self.set_worth(worth)

    def calculation(self, tax):
        """
        Метод для расчета налога на имущество

        :param tax: налог на имущество, параметр передается от дочернего класса.
        :return: результат вычисления налога.
        :rtype: (int)
        """
        result = self.__worth * tax
        return result

    def set_worth(self, worth):
        """
        Сеттер для установления стоимости имущества.

        :param worth: стоимость имущества.
        :type: (int)
        :raise: Если стоимость отрицательная сумма, то вызывается исключение ('Не верна указано сумма.')
        """
        if worth > 0:
            self.__worth = worth
        else:
            raise Exception('Не верна указано сумма.')

    def get_worth(self):
        """
        геттер для получения стоимости имущества.

        :return: __worth
        :rtype: (int)
        """
        return self.__worth

    def __str__(self):
        """
        Метод для вывода данных о название имущества и стоимости.

        :rtype: (str)
        """
        result = ('Название имущества: {property_name}\nСтоимость: {worth}'.format(
            property_name=self.__property_name, worth=self.__worth
        ))
        return result


class Apartment(Property):
    def __init__(self, property_name, worth):
        super().__init__(property_name, worth)
        self.tax = 1/1000

    def tax_calculation(self):
        """
        метод передает в родительский класс стоимость налога и вызывает метод для расчета налога

        :return: результат вычисления налога.
        :rtype: (int)
        """
        return self.calculation(self.tax)


class Car(Property):
    def __init__(self, property_name, worth):
        super().__init__(property_name, worth)
        self.tax = 1/200

    def tax_calculation(self):
        return self.calculation(self.tax)


class CountryHouse(Property):
    def __init__(self, property_name, worth):
        super().__init__(property_name, worth)
        self.tax = 1/500

    def tax_calculation(self):
        return self.calculation(self.tax)


house = Apartment('Дом', 10000000)
car = Car('Lexus', 2000000)

tax_for_pay = house.tax_calculation()
print(house, '\nНалог для оплаты:', tax_for_pay)
