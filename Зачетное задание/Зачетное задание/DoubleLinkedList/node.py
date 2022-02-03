from typing import Any, Optional


class Node:
    """
    Класс, который описывает узел связного списка.
    :value значение узла
    :next_ ссылка на следующий узел
    """

    def __init__(self, value: Any, next_: Optional['Node'] = None):
        self.value = value
        self.next = next_

    @property
    def next(self) -> Optional['Node']:
        """Возвращает ссылку на следующий узел"""
        return self._next

    @next.setter
    def next(self, next_node: Optional['Node'] = None) -> None:
        """установка ссылки на следующий узел"""
        self.is_valid(next_node)
        self._next = next_node

    def __str__(self):
        return f'{self.value}'

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value}, {self.next})'

    @staticmethod
    def is_valid(ch_node: Optional['Node']) -> None:
        """проверка передаваемого значения на соответсвию классу Node или  None"""
        if not isinstance(ch_node, (type(None), Node)):
            raise TypeError


class DoubleLinkedNode(Node):
    def __init__(self, value: Any, next_: Optional['Node'] = None,
                 prev: Optional['Node'] = None):
        super().__init__(value, next_)
        self.prev = prev

    @property
    def prev(self) -> Optional['Node']:
        """ Возвращает ссылку на предыдущий узел"""
        return self._prev

    @prev.setter
    def prev(self, pr_node: Optional[Node] = None) -> None:
        """устанавливает ссылку на предыдущий узел"""
        self.is_valid(pr_node)
        self._prev = pr_node

    def __repr__(self):
        return f'{self.__class__.__name__}({self.value},{self._next},{self.prev})'


if __name__ == "__main__":
    ...
