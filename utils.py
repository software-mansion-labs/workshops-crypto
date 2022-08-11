class FElement:
    mod = 3 * 2**30 + 1

    def __init__(self, val):
        self.val = val % FElement.mod

    def __repr__(self):
        return str(self.val)
    
    def __add__(self, other):
        assert isinstance(other, FElement)
        return FElement((self.val + other.val) % FElement.mod)

    def __sub__(self, other):
        assert isinstance(other, FElement)
        return FElement((self.val - other.val) % FElement.mod)

    def __mul__(self, other):
        assert isinstance(other, FElement)
        return FElement((self.val * other.val) % FElement.mod)
    
    def __eq__(self, other):
        assert isinstance(other, FElement)
        return (self.val % FElement.mod) == (other.val % FElement.mod)

    def __div__(self, other):
        raise NotImplementedError


class Val:
    def __init__(self, i, trace):
        self._index = i
        self._trace = trace

    def next(self) -> "Val":
        return Val(self._index + 1, self._trace) 
    
    @property
    def value(self) -> FElement:
        return self._trace[self._index]


