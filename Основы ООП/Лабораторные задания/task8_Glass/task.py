from typing import Union


# TODO  создать класс Glass
class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.__init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.__init_occupied_volume(occupied_volume)

    @staticmethod
    def check_type_error(value: Union[int, float]) -> None:
        """проверка типа вводимого значениы"""
        if not isinstance(value, (int, float)):
            raise TypeError

    @staticmethod
    def check_value_error(value: Union[int, float]) -> None:
        """
        проверка вводимого значения
        """
        if value < 0:
            raise ValueError

    def __check_error(self, value: Union[int, float]):
        self.check_type_error(value)
        self.check_value_error(value)

    @staticmethod
    def check_overflow(capacity: Union[int, float], occupied: Union[int, float]) -> None:
        if occupied < 0:
            raise ValueError("недолив")
        if (capacity < occupied):
            raise ValueError("перелив")

    def __init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        """
        инициализация значения объема стакана
        :param capacity_volume: объем стакана
        """
        self.__check_error(capacity_volume)
        self.capacity_volume = capacity_volume

    def __init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        """
        инициализация значения объема стакана
        :param capacity_volume: объем стакана
        """
        self.__check_error(occupied_volume)
        self.check_overflow(self.capacity_volume, occupied_volume)
        self.occupied_volume = occupied_volume

    def add_water(self, value: Union[int, float]):
        self.__check_error(value)
        self.check_overflow(self.capacity_volume, self.occupied_volume+value)
        self.occupied_volume += value

    def remove_water(self, value: Union[int, float]):
        self.__check_error(value)
        self.check_overflow(self.capacity_volume, self.occupied_volume-value)
        self.occupied_volume -= value

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)

    glass.add_water(100)
    print(glass.capacity_volume, glass.occupied_volume)

    glass.remove_water(400)
    print(glass.capacity_volume, glass.occupied_volume)


