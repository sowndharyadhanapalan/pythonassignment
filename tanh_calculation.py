"""simple calculator"""
import math


def calculate_tanh(angle):
    """A method to calculate tanh"""
    exponential = math.e
    coshx = ((exponential**angle)+(exponential**-angle))
    sinhx = ((exponential**angle)-(exponential**-angle))
    tanhx = sinhx/coshx
    return tanhx
    unittest.main()
