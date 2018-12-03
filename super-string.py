from collections import defaultdict

class SuperString(str):
    
    def __init__(self, string):
        self._lhs_dict = self._counter(string, defaultdict(int))

    def distance(self, rhs):
        self._rhs_dict = self._counter(rhs, defaultdict(int))
        total_distance = 0
        for i in self._lhs_dict:
            distance = self._lhs_dict[i] - self._rhs_dict[i]
            distance = distance ** 2
            total_distance += distance
        return total_distance
    
    def _counter(self, string, obj):
        for i in string:
            obj[i] += 1
        return obj
