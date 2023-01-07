from vector2 import Vector

v : Vector = Vector(4)
a : Vector = Vector(4)

v[0] = 1
v[3] = 45

a[0] = 1
a[3] = 45

print(a == v)

#print(a in v)