class FuzzySet:
    def __init__(self, iterable: set):
        self.f_set = iterable
        self.f_list = list(iterable)
        self.f_len = len(iterable)
        for elem in self.f_set:
            if not isinstance(elem, tuple):
                raise TypeError("No tuples in the fuzzy set")
            if not isinstance(elem[1], float):
                raise ValueError("Probabilities not assigned to elements")

    def __or__(self, other):
        # fuzzy set union
        if len(self.f_set) != len(other.f_set):
            raise ValueError("Length of the sets is different")
        tmp = []
        f_set = [x for x in self.f_set]
        other = [x for x in other.f_set]
        for i in range(self.f_len):
            tmp.append(f_set[i] if f_set[i][1] > other[i][1] else other[i])
        return FuzzySet(tmp)

    def __and__(self, other):
        # fuzzy set intersection
        if len(self.f_set) != len(other.f_set):
            raise ValueError("Length of the sets is different")
        tmp = []
        f_set = [x for x in self.f_set]
        other = [x for x in other.f_set]
        for i in range(self.f_len):
            tmp.append(f_set[i] if f_set[i][1] < other[i][1] else other[i])
        return FuzzySet(tmp)

    def __invert__(self):
        f_set = [x for x in self.f_set]
        for indx, elem in enumerate(f_set):
            f_set[indx] = (elem[0], float(round(1 - elem[1], 2)))
        return FuzzySet(f_set)

    def __sub__(self, other):
        pass

    def __len__(self):
        return sum([1 for i in self.f_set])

    def __str__(self):
        return f'{[x for x in self.f_set]}'

    def __getitem__(self, item):
        return self.f_list[item]

    def __iter__(self):
        return self.f_list


a = FuzzySet({('x', 0.2), ('y', 0.8)})
b = FuzzySet({('x', 0.3), ('y', 0.3)})
print(f'Fuzzy union: \n{a | b}')

print(f'Fuzzy intersection: \n{a & b}')

print(f'Fuzzy inversion: \n{~a}')
