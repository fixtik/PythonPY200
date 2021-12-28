from typing import Union, Any

import plotly.graph_objs as go


class Cube:
    """
    класс для работы с кубом
    """

    def __init__(self, len_a: Union[int, float],
                 color: (int, int, int) = (255, 255, 255),
                 border_width: Union[int, float] = 0,
                 border_color: (int, int, int) = (255, 255, 255)):
        """
        :param len_a: сторона куба
        :param color: цвет заливки куба
        :param border_width: ширина рамки
        :param border_color: цвет рамки
        """

        self.__a = self.__check_a(len_a)
        self.__color = self.__check_color(color)
        self.__border_width = self.__check_border_width(border_width)
        self.__border_color = self.__check_color(border_color)

    @staticmethod
    def __check_type(incoming_type: Any, comp_type: Any, msg: str = '') -> None:
        """
        :rtype: object
        :param incoming_type: тип переменной для сравнения
        :param comp_type: эталонный тип
        :param msg: название переменной для вывода ошибки
        """
        if not isinstance(incoming_type, comp_type):
            raise TypeError(msg)

    @staticmethod
    def __check_value(incoming_value: Any,
                      left_bool=(False, False), left_side: Any = 0,
                      right_bool=(False, False), right_side: Any = 0,
                      msg: str = '') -> None:
        """
        Проверка значений по критериям
        :param incoming_value: проверяемое значение
        :param left_side: минимально-допустимое значение
        :param right_side: максимально допустимое значение (опционально)
        :param left_bool: кортеж со значениями (необходимость левой границы, строгое неравенство)
        :param right_bool: кортеж со значениями (необходимость правой границы, строгое неравенство)
        :param msg: название переменной для сообщения об ошибке
        """
        if left_bool[0]:
            if left_bool[1]:
                if incoming_value < left_side:
                    raise ValueError(f'Параметр "{msg}" не может быть меньше {left_side}')
            else:
                if incoming_value <= left_side:
                    raise ValueError(f'Параметр "{msg}" не может быть меньше или равен {left_side}')

        if right_bool[0]:
            if right_bool[1]:
                if incoming_value > right_side:
                    raise ValueError(f'Параметр "{msg}" не может быть больше {right_side}')
            else:
                if incoming_value >= right_side:
                    raise ValueError(f'Параметр "{msg}" не может быть больше или равен {right_side}')

    def __check_a(self, value: Union[int, float]) -> Union[int, float]:
        """
        проверка введеных значений.
        :param value: предлагаемое значение
        :return: проверенное значение
        """
        self.__check_type(value, (int, float), "Длина должна быть задана только числовым значением!")
        self.__check_value(value, (True, True), msg='Длина')
        return value

    def __check_border_width(self, value: Union[int, float]) -> Union[int, float]:
        """
        проверка введенного значения ширины рамки
        :param value: предлагаемое значение
        :return: возвращаемое значение
        """
        self.__check_type(value, (int, float), "Ширина рамки задается числом!")
        self.__check_value(value, (True, True), 0, (True, True), self.__a, "Ширина рамки")
        return value

    def __check_color(self, incoming_val: (int, int, int)) -> int:
        """
        Проверка введенных значений для цвета
        :param incoming_val: кортеж с тремя значениями RGB
        :return: возвращаемое значение
        """
        for i in range(len(incoming_val)):
            self.__check_type(incoming_val[i], int, "Цвет задается целочисленным значнием!")
        for i in range(len(incoming_val)):
            self.__check_value(incoming_val[i], (True, False), right_bool=(True, True), right_side=255, msg="Цвет")
        return incoming_val

    def get_len_a(self) -> Union[int, float]:
        """
        Возвращает текущее значение длины стороны куба
        """
        return self.__a

    def set_len_a(self, new_value: Union[int, float]) -> None:
        """
        Устанавливает новое значение длины стороны
        :param new_value: передаваемое значение
        """
        self.__a = self.__check_a(new_value)

    def get_border_width(self) -> Union[int, float]:
        """
        Возвращает текущее значение ширины рамки
        """
        return self.__border_width

    def set_border_width(self, new_value: Union[int, float]) -> None:
        """
        Устанавливает новое значение ширины рамки
        :param new_value: передаваемое значение
        """
        self.__border_width = self.__check_border_width(new_value)

    def get_color(self)-> str:
        """
        Возвращает строку rgb(кортеж RGB объекта)
        """
        return f'rgb{self.__color}'

    def set_color(self, color_rgb: (int, int, int)) -> None:
        """
        Устанавливает цвет объекта
        :param color_rgb: предлашаемый цвет в формате RGB
        """
        self.__check_color(color_rgb)
        self.__color = color_rgb

    def get_border_color(self) -> (int, int, int):
        """
        Возвращает строку rgb(кортеж RGB объекта)
        """
        return f'rgb{self.__border_color}'

    def set_border_color(self, color_rgb: (int, int, int)) -> None:
        """
        Устанавливает цвет рамки
        :param color_rgb: предлашаемый цвет в формате RGB
        """
        self.__check_color(color_rgb)
        self.__border_color = color_rgb

    def __str__(self):
        return f'сторона куба = {self.__a} цвет заливки (R={self.__color[0]}, G={self.__color[1]}, ' \
               f'B={self.__color[2]}) \nширина рамки {self.__border_width}, цвет рамки (R={self.__border_color[0]}, ' \
               f'G={self.__border_color[1]}, B={self.__border_color[2]}'

    def __repr__(self):
        return f'Cube({self.__a}, {self.__color}, {self.__border_width}, {self.__border_color})'

    def square_cube(self) -> Union[int, float]:
        """
        нахождение площади куба
        :return: площадь куба
        """
        return 6 * (self.__a ** 2)

    def square_side(self) -> Union[int, float]:
        """
        нахождение площади стороны куба
        :return: площадь стороны куба
        """
        return self.__a ** 2

    def volume(self) -> Union[int, float]:
        """
        получение объема куба
        :return: объем куба
        """
        return self.__a ** 3

    def draw_square(self) -> None:
        """
        Отображение квадрата с помощью plotly
        """
        start = 5 # точка отсчета
        fig = go.Figure()
        fig.add_trace(go.Scatter(x=[start], y=[start], mode="markers"))
        fig.add_shape(type='rect', x0=start, y0=start, x1=start + self.get_len_a(), y1=start + self.get_len_a(),
                      fillcolor=self.get_color())
        fig.add_shape(type="rect", x0=start, y0=start, x1=start + self.get_len_a(), y1=start + self.get_len_a(),
                      line=dict(color=self.get_border_color(), width=self.get_border_width()))

        fig.update_layout(autosize=False, width=start + 500, height=start + 500,
                          margin=dict(l=50, r=50, b=100, t=100, pad=4),
                          paper_bgcolor="LightSteelBlue")
        fig.show()

    # def draw_cube(self) -> None:
    #     """
    #     Отображение куба  с помощью plotly
    #     """
    #     start = 0
    #     a = start + (self.get_len_a()) * 10
    #     # x = [a, a, start, start, a, a, start, start]
    #     # y = [start, a, a, start, start, a, a, start]
    #     # z = [start, start, start, start, a, a, a, a]
    #     x = [0, 0, 0, 0, 100, 100, 100, 100]
    #     y = [100, 0, 100, 0, 100, 0, 100, 0]
    #     z = [100, 100, 0, 0, 100, 100, 0, 0]
    #     # fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z,
    #     #                                 opacity=0.5,
    #     #                                 color='rgba(244,22,100,0.6)'
    #     #                                 )])
    #     fig = go.Figure(data=[go.Mesh3d(x=x, y=y, z=z, i=y, j=z, k=x, color='lightpink', opacity=0.50)])
    #     # fig = go.Figure(data=[
    #     #     go.Scatter3d(x=x, y=y, z=z,
    #     #                  mode='markers',
    #     #                  marker=dict(size=2)
    #     #                  ),
    #     #     go.Scatter3d(
    #     #         # 8 vertices of a cube
    #     #         x=x,
    #     #         y=y,
    #     #         z=z,
    #     #
    #     #         # i=[7, 0, 0, 0, 4, 4, 6, 6, 4, 0, 3, 2],
    #     #         # j=[3, 4, 1, 2, 5, 6, 5, 2, 0, 1, 6, 3],
    #     #         # k=[0, 7, 2, 3, 6, 7, 1, 1, 5, 5, 7, 6],
    #     #         opacity=0.6,
    #     #         # color='#DC143C',
    #     #         # flatshading=True
    #     #     )
    #     # ])
    #
    #     fig.update_layout(
    #         scene=dict(
    #             xaxis=dict(nticks=4, range=[-100, 100], ),
    #             yaxis=dict(nticks=4, range=[-50, 100], ),
    #             zaxis=dict(nticks=4, range=[-100, 100], ), ),
    #         width=700,
    #         margin=dict(r=20, l=10, b=10, t=10))
    #     fig.show()


cube = Cube(15, color=(1, 5, 1), border_width=10, border_color=(90,255, 240))
print(cube)

print(list(Cube(i) for i in range(5)))

cube.draw_square()