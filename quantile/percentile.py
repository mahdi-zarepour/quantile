"""
Percentile
"""
import math


class Percentile:
    def __init__(self, data, p):
        self.data = data
        self.data.sort()
        self.p = p
        self.p_checker(self.p)

    def p_checker(self, p):
        if isinstance(p, int) and (1 < p < 100):
            return True
        else:
            raise ValueError('p must be a positive integer and less than 100')

    def recognize_data_index(self):
        init_id = ((len(self.data) + 1) * self.p) / 100
        _int_part = math.modf(init_id)[1]
        _float_part = math.modf(init_id)[0]
        return _int_part, _float_part

    def percentile_calculator(self):
        _int_part, _float_part = self.recognize_data_index()
        a =  self.data[int(_int_part - 1)]
        b = self.data[int(_int_part)]
        part_1 = (1 - _float_part) * self.data[int(_int_part - 1)]
        part_2 = _float_part * self.data[int(_int_part)]
        return part_1 + part_2


__all__ = [
    'Percentile',
]
