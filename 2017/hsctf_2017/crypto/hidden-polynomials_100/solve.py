#! /usr/bin/env python3
##
from gmpy2 import *
p_2017 = 49189926321482294101673925793095

year = 2017
guess = 0

# Find coefficients
coefficients = []
for power in reversed(range(10)):
    previous_coeff = 0
    previous_attempt = 0
    for coefficient in range(1000):
        attempt = (coefficient * pow(year, power))
        attempt_subtract = p_2017 - guess - attempt
        if (attempt_subtract < 0):
            coefficients.append(str(previous_coeff))
            guess += previous_attempt
            break
        previous_coeff = coefficient
        previous_attempt = attempt

# Check calculations are correct
total = 0
for k, coefficient in enumerate(reversed(coefficients)):
    total += int(coefficient) * pow(year, k)
assert total == p_2017

# Calculate for P(1)
p_1 = 0
for k, coefficient in enumerate(reversed(coefficients)):
    p_1 += int(coefficient) * pow(1, k)

print("Flag: %d" % p_1)