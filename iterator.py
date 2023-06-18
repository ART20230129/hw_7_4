
##Доработать класс FlatIterator в коде ниже. Должен получиться итератор, ,
##который принимает список списков и возвращает их плоское представление,
##т. е. последовательность, состоящую из вложенных элементов.
##Функция test в коде ниже также должна отработать без ошибок.

class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.outer_cursor = 0
        self.inner_cursor = 0

    def __iter__(self):

        return self


    def __next__(self):
        if self.outer_cursor >= len(self.list_of_list) or self.inner_cursor >= len(self.list_of_list[self.outer_cursor]):
            raise StopIteration
        else:
            item = self.list_of_list[self.outer_cursor][self.inner_cursor]
            self.inner_cursor += 1
            if self.inner_cursor >= len(self.list_of_list[self.outer_cursor]):
                self.outer_cursor += 1
                self.inner_cursor = 0
        return item

##Тест работы итератора
##list_of_lists = [
##    ['a', 'b', 'c'],
##    ['d', 'e', 'f', 'h', False],
##    [1, 2, None]
##]
##
##print(list(FlatIterator(list_of_lists)))



def test_1():

    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):

        assert flat_iterator_item == check_item

    assert list(FlatIterator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]


if __name__ == '__main__':
    test_1()