from polynomial import Polynomial, interpolate_poly
from field import FieldElement as FElement

def test_polynomial(is_polynomial):
    assert is_polynomial(1, [FElement(0), FElement(1), FElement(2)], [FElement(1), FElement(1), FElement(1)])
    assert not is_polynomial(1, [FElement(0), FElement(1), FElement(2)], [FElement(1), FElement(1), FElement(2)])
    
    d_3 = interpolate_poly([FElement(1), FElement(2), FElement(3)], [FElement(2), FElement(1), FElement(2)])
    domain = 100
    assert is_polynomial(3, [FElement(x) for x in range(1, domain)], [d_3(FElement(x)) for x in range(1, domain)])
    assert not is_polynomial(2, [FElement(x) for x in range(1, domain)], [d_3(FElement(x)) for x in range(1, domain)])
    assert not is_polynomial(1, [FElement(x) for x in range(1, domain)], [d_3(FElement(x)) for x in range(1, domain)])
