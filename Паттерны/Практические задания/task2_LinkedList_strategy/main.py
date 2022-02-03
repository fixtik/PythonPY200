from typing import Iterable

from linked_list import LinkedList
from drivers import IStructureDriver
from factory_method import SimpleFileFactoryMethod


class LinkedListWithDriver(LinkedList):
    def __init__(self, data: Iterable = None, driver: IStructureDriver = None):
        super().__init__(data)
        self.driver = driver


    def read(self):
        """ С помощью драйвера считать данные и поместить их в LinkedList. """
        data_driver = self.driver.read()
        for data in data_driver:
            self.append(data)


    def write(self):
        """ С помощью драйвера записать данные из LinkedList. """
        self.driver.write(self)


if __name__ == '__main__':
    ll = LinkedListWithDriver()
    print("Считать данные из файла input.txt")
    ll.driver = SimpleFileFactoryMethod.get_driver()

    ll.read()
    print(ll)

    print("Записать данные в файл по умолчанию")
    ll.driver = SimpleFileFactoryMethod.get_driver()
    ll.write()