"""
Quartile
"""
import math


class Quartile:
    def __init__(self, data, q):
        self.data = data
        self.data.sort()
        self.q = q
        self.q_checker(self.q)
    
    def q_checker(self, q):
        if isinstance(q, int) and (0 < q < 4):
            return True
        else:
            raise ValueError('q must be a positive integer and less than 4')

    def recognize_data_index(self):
        init_id = ((len(self.data) + 1) * self.q) / 4
        _int_part = math.modf(init_id)[1]
        _float_part = math.modf(init_id)[0]
        return _int_part, _float_part

    def quartile_calculator(self):
        _int_part, _float_part = self.recognize_data_index()
        part_1 = (1 - _float_part) * self.data[int(_int_part - 1)]
        part_2 = _float_part * self.data[int(_int_part)]
        return part_1 + part_2


__all__ = [
    'Quartile',
]
