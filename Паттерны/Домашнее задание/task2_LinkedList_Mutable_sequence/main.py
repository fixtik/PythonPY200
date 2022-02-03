from abc import ABC
from collections.abc import MutableSequence
from typing import Any, Optional, Iterable

class Node:
    """ Класс, который описывает узел связного списка. """

    def __init__(self, value: Any, next_: Optional["Node"] = None):
        """
        Создаем новый узел для односвязного списка
        :param value: Любое значение, которое помещено в узел
        :param next_: следующий узел, если он есть
        """
        self.value = value

        self.next = None
        self.set_next(next_)

    def __repr__(self) -> str:
        return f"Node({self.value}, {None})" if self.next is None else f"Node({self.value}, Node({self.next}))"

    def __str__(self) -> str:
        return str(self.value)

    def is_valid(self, node: Any) -> None:
        if not isinstance(node, (type(None), Node)):
            raise TypeError

    def set_next(self, next_: Optional["Node"] = None) -> None:
        self.is_valid(next_)
        self.next = next_


class LinkedList(MutableSequence):

    def __init__(self, data: Iterable = None):
        """Конструктор связного списка"""
        self.len = 0
        self.head: Optional[Node] = None

        if data is not None:
            for value in data:
                self.append(value)

    def append(self, value: Any):
        """ Добавление элемента в конец связного списка. """
        append_node = Node(value)

        if self.head is None:
            self.head = append_node
        else:
            last_index = self.len - 1
            last_node = self.step_by_step_on_nodes(last_index)

            self.linked_nodes(last_node, append_node)

        self.len += 1

    def __len__(self):
        return self.len

    @staticmethod
    def linked_nodes(left_node: Node, right_node: Optional[Node] = None) -> None:
        """
        Функция, которая связывает между собой два узла.

        :param left_node: Левый или предыдущий узел
        :param right_node: Правый или следующий узел
        """
        left_node.set_next(right_node)

    def step_by_step_on_nodes(self, index: int) -> Node:
        """ Функция выполняет перемещение по узлам до указанного индекса. И возвращает узел. """
        if not isinstance(index, int):
            raise TypeError()
        if not 0 <= index < self.len:  # для for
            raise IndexError()
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def __getitem__(self, index: int) -> Any:
        """ Метод возвращает значение узла по указанному индексу. """
        return self.step_by_step_on_nodes(index).value

    def to_list(self) -> list:
        return [value for value in self]

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}({self.to_list()})'

    def __str__(self) -> str:
        return f'{self.to_list()}'

    def __setitem__(self, key: int, value: Any):
        """
        устанавливает значение узла по ключу
        """
        self.step_by_step_on_nodes(key).value = value

    def __delitem__(self, key: int):
        """удаляет узел по ключу"""
        del_node = self.step_by_step_on_nodes(key)

        if del_node is self.head:
            self.head = del_node.next
            del del_node
        else:
            prev_node = self.step_by_step_on_nodes(key-1)
            self.linked_nodes(prev_node,del_node.next)
            del del_node
        self.len -= 1


if __name__ == "__main__":
        ...
