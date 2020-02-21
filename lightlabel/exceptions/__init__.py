class ItemNotInException(Exception):
    def __init__(self, item):
        super().__init__(self)
        self.item = item

    def __str__(self):
        return "ItemNotInException: {} not in given choices".format(self.item)


class CantSerializeException(Exception):
    def __init__(self, obj):
        super().__init__()
        self.obj = obj

    def __str__(self):
        return "the object can't be serialized!".format(id(self.obj))


if __name__ == '__main__':
    # raise ItemNotInException('c')
    raise CantSerializeException('c')
