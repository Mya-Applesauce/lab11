"""
Rotation test
Ari Papke
testing rotation_utils
04/10/26
"""

import pytest
from rotation_utils import adjust_rotation

def test_rotation_utils():
    adjusted_rotation = adjust_rotation(100)
    assert adjusted_rotation == 100

def test_rotation_utils2():
    adjusted_rotation = adjust_rotation(460)
    assert adjusted_rotation == 100

def test_rotation_utils3():
    adjusted_rotation = adjust_rotation(820)
    assert adjusted_rotation == 100

def test_rotation_utils4():
    adjusted_rotation = adjust_rotation(-100)
    assert adjusted_rotation == 260

def test_rotation_utils5():
    adjusted_rotation = adjust_rotation(-460)
    assert adjusted_rotation == 260

def test_rotation_utils6():
    adjusted_rotation = adjust_rotation(-820)
    assert adjusted_rotation == 260

def test_rotation_utils7():
    with pytest.raises(TypeError, match='Input must be a numeric value.') as excinfo:
        adjust_rotation("ur mom")
