class Vector:
    values = []

    def __init__(self, values):
        for v in values:
            if not isinstance(v, int):
                raise Exception("v values must be numbers.")
        self.values = list(values)

    def __repr__(self):
        return repr(self.values)

    def __str__(self):
        if not len(self.values):
            return "Vector()"
        string = str(self.values[0])
        for value in self.values[1:]:
            string = string + ", " + str(value)
        return "Vector({})".format(string)

    def __len__(self):
        return len(self.values)

    def __eq__(self, other):
        if isinstance(other, Vector):
            if len(self.values)!=len(other.values):
                return False
            for i in range(len(self.values)):
                if self.values[i] != other.values[i]: return False
            return True
        else:
            return False

    def __add__(self, other):
        return Vector(list(map(lambda x, y: x + y, self.values, other.values)))

    def __sub__(self, other):
        return Vector(list(map(lambda x, y: x - y, self.values, other.values)))

    def __mul__(self, other):
        if isinstance(other, Vector):
            sum = 0
            for i in range(len(self.values)):
                sum += self.values[i] * other.values[i]
            return sum
        elif type(other) is int or type(other) is float:
            result = Vector(self.values)
            for i in range(len(self.values)):
                result.values[i] *= other
            return result

    def __iadd__(self, other):
        self.values = (list(map(lambda x, y: x + y, self.values, other.values)))
        return self

    def __isub__(self, other):
        self.values = (list(map(lambda x, y: x - y, self.values, other.values)))
        return self

    def __getitem__(self, item):
        if type(item)!=int:
            raise Exception("item must be numbers")
        else:
            if 0 <= item < len(self.values):
                return self.values[item]


    def __setitem__(self, key, value):
        if type(value)!=int:
            raise Exception("key must be numbers")
        else:
            if 0 <= key < len(self.values):
                self.values[key] = value
                return self



    def __neg__(self):
        return Vector(list(map(lambda x: -x, self.values)))

    def __bool__(self):
        if len(self.values) != 0:
            return True
        else:
            return False

    def __abs__(self):
        sum = 0
        for i in self.values:
            sum += i ** 2
        sum = sum ** (0.5)
        return sum
