from typing import Union


# TODO  создать класс Glass
class Glass:

    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        self.capacity_volume = None
        self.__init_capacity_volume(capacity_volume)
        self.occupied_volume = None
        self.__init_occupied_volume(occupied_volume)

    def __init_capacity_volume(self, capacity_volume: Union[int, float]) -> None:
        """
        инициализация значения объема стакана
        :param capacity_volume: объем стакана
        """
        self.capacity_volume = capacity_volume

    def __init_occupied_volume(self, occupied_volume: Union[int, float]) -> None:
        """
        инициализация значения объема стакана
        :param capacity_volume: объем стакана
        """
        self.occupied_volume = occupied_volume

if __name__ == "__main__":
    glass = Glass(200, 100)  # экземпляр класса
    print(glass.capacity_volume, glass.occupied_volume)
