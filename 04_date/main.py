class Date:
    """
    Класс для проверки даты на корректность.

    :args:
        day(int): День
        month(int): Месяц
        year(int): Год
    """
    def __init__(self, day: int, month: int, year: int) -> None:
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def from_string(cls, data: str) -> object:
        """
        Метод, конвертирует строку доты в объект класса.

        :args:
            data(str): Дата в виде строки.
        :return:
            result(object)

        """
        data = data.split('-')
        day, month, year = int(data[0]), int(data[1]), int(data[2])
        result = cls(day, month, year)
        return result

    @classmethod
    def is_date_valid(cls, data: str) -> bool:
        """
        Метод, для проверки на корректность даты.

        :args:
            data(str): дата

        :return(bool)

        """
        data = data.split('-')
        day, month, year = int(data[0]), int(data[1]), int(data[2])
        if 1 <= day <= 31 and 1 <= month <= 12 and 1 <= year <= 5000:
            return True
        return False

    def __str__(self) -> str:
        """
        Метод, выводит на экран день, месяц, год.

        """
        return 'День: {}  Месяц: {}   Год: {}'.format(
            self.day, self.month, self.year)


date = Date.from_string('10-12-2077')
print(date)
print(Date.is_date_valid('10-12-2077'))
print(Date.is_date_valid('40-12-2077'))
