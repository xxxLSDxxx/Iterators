class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list

    def __iter__(self):
        self.main_list_cursor = 0
        self.nested_list_cursor = 0
        return self

    def __next__(self):
        if self.main_list_cursor == len(self.list_of_list):
            raise StopIteration
        item_main_cursor = self.list_of_list[self.main_list_cursor]
        item_nested_cursor = item_main_cursor[self.nested_list_cursor]
        self.nested_list_cursor += 1
        if self.nested_list_cursor == len(item_main_cursor):
            self.nested_list_cursor = 0
            self.main_list_cursor += 1
        return item_nested_cursor


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
    