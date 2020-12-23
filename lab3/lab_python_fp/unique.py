class Unique(object):
    def __init__(self, items, **kwargs):
        self.used_elements = set()
        self.items = iter(items)
        if 'ignore_case' not in kwargs:
            self.ignore_case = False
        else:
            self.ignore_case = kwargs['ignore_case']

    def __next__(self):
        while True:
            current = self.items.__next__()
            if self.ignore_case:
                current = current.lower()
            if current not in self.used_elements:
                self.used_elements.add(current)
                return current

    def __iter__(self):
        return self


if __name__ == "__main__":
    data = ['A', 'a', 'b', 'c', 'B']
    unique = Unique(data, ignore_case=True)
    for i in unique:
        print(i, end=' ')
    print('\n')

    data2 = ['A', 'a', 'b', 'c', 'B']
    unique = Unique(data, ignore_case=False)
    for i in unique:
        print(i, end=' ')
