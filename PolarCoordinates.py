import cmath

z = complex(input())
x = z.real
y = z.imag

phi = abs(complex(x, y))
r = cmath.phase(z)

print(phi)
print(r)
