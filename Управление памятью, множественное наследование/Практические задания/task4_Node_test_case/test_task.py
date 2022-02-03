import unittest

from task import Node


class TestCase(unittest.TestCase):
    def test_init_node_without_next(self):
        """Проверить следующий узел после инициализации с аргументом next_ по умолчанию"""
        node = Node('test node')
        msg = 'default = None'
        self.assertIsNone(node.next, msg)  # TODO с помощью метода assertIsNone проверить следующий узел

    def test_init_node_with_next(self):
        """Проверить следующий узел после инициализации с переданным аргументом next_"""
        rigth_node = Node('right')
        left_node = Node('left', rigth_node)
        self.assertEqual(repr(left_node.next), repr(rigth_node), 'Error')
        ...  # TODO проверить что узлы связались

    def test_repr_node_without_next(self):
        """Проверить метод __repr__, для случая когда нет следующего узла."""
        node = Node('empty node')
        repr_node = "Node(empty node, None)"
        self.assertEqual(repr(node), repr_node, "Error `repr")
        ...  # TODO проверить метод __repr__ без следующего узла

    @unittest.skip
    def test_repr_node_with_next(self):
        """Проверить метод __repr__, для случая когда установлен следующий узел."""
        ...

    def test_str(self):
        some_value = 5
        node = Node(some_value)
        self.assertEqual(str(some_value), str(node.value), 'error str')
        # TODO проверить строковое представление

    def test_is_valid(self):
        Node.is_valid(None)
        Node.is_valid(Node("correct_node"))

        with self.assertRaises(TypeError):
            Node.is_valid("incorrect_type")
        # TODO с помощью менеджера контакста и метода assertRaises проверить корректность вызываемой ошибки
