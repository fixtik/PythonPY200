class Date:
    """Класс для работы с датами"""
    DAY_OF_MONTH = (
        (31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31),  # обычный год
        (31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)  # високосный
    )

    __slots__ = ('day', 'month', 'year')

    def __init__(self, day: int, month: int, year: int):
        self.day = day
        self.month = month
        self.year = year

        self.is_valid_date(self.day, self.month, self.year)

    @staticmethod
    def is_leap_year(year: int):
        """Проверяет, является ли год високосным"""
        return True if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0) else False


    def get_max_day(self, month: int, year: int) -> int:
        """Возвращает максимальное количество дней в месяце для указанного года"""
        if self.is_leap_year(year):
            return self.DAY_OF_MONTH[1][month-1]
        else:
            return self.DAY_OF_MONTH[0][month-1]

    def is_valid_date(self, day: int, month: int, year: int):
        """Проверяет, является ли дата корректной"""
        if not (isinstance(day, int) & isinstance(month, int) & isinstance(year, int)):
            raise TypeError('Вводите целочисленные значения')
        if not((1 <= day <= 31) & (1 <= month <= 12) & year >= 0):
            raise ValueError('Превышен диапазон возможных значений!')
        if not (day <= self.DAY_OF_MONTH[0][month-1] or day <= self.DAY_OF_MONTH[1][month-1]):
            raise ValueError('Проверьте корректность введенных данных')
        if self.get_max_day(month, year) < day:
            raise ValueError('В этом месяце не может быть так много дней')
        self.day = day
        self.month = month
        self.year = year

if __name__ == "__main__":
    # Write your solution here
    calen = Date(9,1,-1)

