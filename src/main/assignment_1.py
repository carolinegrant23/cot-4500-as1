import numpy as np
import struct


binary_number = 0b0100000001111110101110010000000000000000000000000000000000000000

buffer = binary_number.to_bytes(8,'big')

#question 1: 
double_precision = struct.unpack('>d', buffer)[0]
print(f'{double_precision:.5f}')

#question 2:
chop = int(double_precision)
print(chop)

#question 3:
round_ = round(double_precision, 0)
print(round_)

#question 4: 
absolute_error = (double_precision - round_)
print(absolute_error)

relative_error = (absolute_error / double_precision)
print(relative_error)

#question 5: 
k = x = 1
# while True:
for i in range(10):
    series = ((-1)**k * (x**k / k**3)) 
    print(k, x, series)
    k += 1
