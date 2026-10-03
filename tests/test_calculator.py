import pytest
from practice.calculator import calculator
class TestCalculator:
    @pytest.mark.skipif(1==4,reason="meiyouliyou")
    def test_add_int(self):
        cal=calculator()
        assert cal.add(1,2)==3
        assert cal.add(-1,-4)==-5

    def test_add_float(self):
        cal=calculator()
        assert cal.add(1.5,2.6)==4.1

