from typing import Union


class Glass:
    def __init__(self, capacity_volume: Union[int, float], occupied_volume: Union[int, float]):
        if isinstance(capacity_volume, (int, float)) and isinstance(occupied_volume, (int, float)):
            if 0 < capacity_volume and capacity_volume >= occupied_volume >=0:
                self.capacity_volume = capacity_volume
                self.occupied_volume = occupied_volume
            else:
                raise ValueError('Вы ввкели некорректные значения')
        else:
            raise TypeError('Вы ввели некорректные данные')



if __name__ == "__main__":
        glass1 = Glass(200, 100)
        glass2 = Glass(300, 300)

        error_glass = Glass(-300,100)



