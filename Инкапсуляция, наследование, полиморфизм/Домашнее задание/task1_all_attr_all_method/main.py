class Parent:
    """
    класс описывающий носитель информации и его логическое разбиение
    """
    drive_name = None  # название носителя
    _drive_type = None  # тип носителя
    __drive_count = 0  # количество носителей

    def __init__(self, drive_number: int):

        self.drive_number = drive_number  # номер носителя в операционной системе
        self._serial_number = None  # серийный номер носителя
        self.__vendor = None  # производитель носителя информации

        self.__class__.__drive_count = self.__class__.__add_drive()

    def get_count_partitions(self) -> int :
        """
        возвращает количество разделов на носителе
        """
        part_count = 0
        ...
        return part_count

    def _get_serial_number(self) -> str:
        """
        получает серийный номер носителя из ОС
        :return: серийный номер
        """
        ser_num = ''
        ...
        return ser_num

    def __get_start_sector(self) -> int:
        """
        возвращает стартовый сектор раздела
        """
        start_sect = 0
        ...
        return start_sect

    @classmethod
    def change_drive_name(cls, new_name: str) -> None:
        """
        изменяет имя носителя (в классе)
        :param new_name: новое имя носителя
        """
        cls.drive_name = new_name
        return cls.drive_name

    @classmethod
    def get_drive_count(cls):
        return cls.__drive_count

    @classmethod
    def _change_drive_type(cls, new_type: str) -> None:
        """
        Изменяет тип носителя
        :param new_type: новое название типа носителя
        """
        cls._drive_type = new_type
        return cls._drive_type

    @classmethod
    def __add_drive(cls):
        """
        увеличивает количество разделов на 1
        :return:
        """
        cls.__drive_count += 1
        return cls.__drive_count

    @staticmethod
    def get_drive_count_sector(drive_size_in_byte: int, sector_size=512) -> int:
        """
        возвращает количество секторов на носителе
        :param drive_size_in_byte: размер носителя в байтах
        :param sector_size: размер сектора в байтах
        :return: количество секторов
        """
        return drive_size_in_byte // sector_size

    @staticmethod
    def _get_partition_fs_type(boot_sect: bytearray) -> str:
        """
        Определяет тип ФС носителя по загрузочному сектору раздела
        :param boot_sect: бит массив загрузочного сектора
        :return: тип фс
        """
        fs_type = ''
        ...
        return fs_type

    @staticmethod
    def __get_volume_count_from_mbr(mbr_array: bytearray) -> int:
        """
        получение количества разделов на носителе из MBR
        :param mbr_array: бит массив MBR
        :return: количество разделов
        """
        part_count = 0
        ...
        return part_count


class Child(Parent):
    pass





if __name__ == "__main__":

    parent = Parent(0)
    parent.change_drive_name('Western Digital')
    parent._change_drive_type('НЖМД')

    print(parent.get_drive_count())
    print(parent.drive_name)

    child = Child(2)
    print(child.drive_name)
    print(child.get_drive_count_sector(17179869184))