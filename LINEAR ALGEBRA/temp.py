import numpy as np
# u = (2, 3, 4)
# v = (1, 5, 6)

u1=list(map(int,input("Enter vector u (3 elements): ").split()))
v1=list(map(int,input("Enter vector v (3 elements): ").split()))

u=np.array(u1)
v=np.array(v1)
print("The vector u is:",u)
print("The vector v is:",v)

add=u+v
print("Vector addition is:",add)

scalar=int(input("Enter a scalar:"))
print("The scalar multiplication is:",scalar*u)
print("The dot product(U.V):",sum(u*v))

print("The cross product of UxV is:",np.cross(u,v))
dot=sum(u*v)
if dot==0:
    print("Vectors are orthogonal")
else:
    print("Vectors are not orthogonal")
k=u*2
if sum(v)==sum(k):
    print("Vector are parallel")
else:
    print("vector are not parallel")