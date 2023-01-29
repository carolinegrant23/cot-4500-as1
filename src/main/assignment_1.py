import struct

binary_number = 0b0100000001111110101110010000000000000000000000000000000000000000

buffer = binary_number.to_bytes(8,'big')

#question 1: 
double_precision = struct.unpack('>d', buffer)[0]
print(f'{double_precision:.4f}')
print()

#question 2:
chop = float(int(double_precision))
print(chop)
print()

#question 3:
round_ = round(double_precision, 0)
print(round_)
print()

#question 4: 
absolute_error = (abs(double_precision - round_))
print(absolute_error)

relative_error = (absolute_error / double_precision)
print(relative_error)
print()

#question 5: 
k = x = 1
value = ((-1)**k * (x**k / k**3))
delta = abs(value)
ERROR = 10**-4
while delta > ERROR :
    value = ((-1)**k * (x**k / k**3))
    delta = abs(value)
    k += 1
print(k-2)
print()

#question 6 part a:
tol = 10**-4
left = -4
right = 7
def f(x):
    return x**3 + 4*(x**2) - 10


i = 0
while(abs(right - left) > tol):
    i += 1
    p = (left + right) / 2
    if((f(left) < 0 and f(p) > 0) or (f(left) > 0 and f(p) < 0)):
        right = p 
    else:
        left = p
print(i)
print()

#question 6 part b: 

def custom_derivative(value):
    return (3 * value* value) + (8 * value)

def f(x):
    return x**3 + 4*(x**2) - 10

def newton_raphson(initial_approximation: float, tolerance: float):
    iteration_counter = 0
    x = initial_approximation
    f_x = f(x)
    f_prime = custom_derivative(initial_approximation)
    approximation: float = f_x / f_prime
    while(abs(approximation) >= tolerance):
        x = initial_approximation
        f_x = f(x)
        f_prime = custom_derivative(initial_approximation)
        approximation = f_x / f_prime
        initial_approximation -= approximation
        iteration_counter += 1
    return iteration_counter 

if __name__ == "__main__":
    initial_approximation: float = 7
    tolerance: float = .0001
    result = newton_raphson(initial_approximation, tolerance)
    print(result)
    print()
