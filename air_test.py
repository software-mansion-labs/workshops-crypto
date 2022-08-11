from utils import FElement, Val


def test_air(air_class):
    air = air_class()
    test_trace(air.build_trace())
    test_assertions(air)
    test_constraints_continous(air)

def test_trace(trace):
    first = FElement(12)
    res = [first]
    for i in range(21):
        res.append(first*(first*first) + FElement(1))
        first = res[-1]
    assert trace == res
    assert all(isinstance(x, FElement) for x in trace)

def test_assertions(air):
    first = FElement(14)
    res = [first]
    for i in range(21):
        res.append(first*(first*first) + FElement(1))
        first = res[-1]
    assert any((x != FElement(0)) for x in air.resolve_assertions(res))

    first = FElement(12)
    res = [first]
    for i in range(21):
        res.append(first*(first*first) + FElement(1))
        first = res[-1]
    assert all((x == FElement(0)) for x in air.resolve_assertions(res))

def test_constraints_continous(air):
    first = FElement(12)
    res = [first]
    for i in range(21):
        res.append((first*first) + FElement(2))
        first = res[-1]

    for i in range(20):
        assert air.resolve_constraint(Val(i, res)) != FElement(0)


    first = FElement(12)
    res = [first]
    for i in range(21):
        res.append(first*(first*first) + FElement(1))
        first = res[-1]

    for i in range(20):
        assert air.resolve_constraint(Val(i, res)) == FElement(0)



