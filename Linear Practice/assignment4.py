import numpy as np
u=np.array(list(map(int,input("Enter u vector:").split())))
v=np.array(list(map(int,input("Enter v vectir:").split())))

print("U+V=",u+v)
print("2*U=",2*u)
print("U.V=",np.dot(u,v))
dot=np.dot(u,v)
if dot==0:
    print("Yes")
else:
    print("Not")
#caushy schwarz
#|u.v|<=||u||+||v||
norm_u=np.linalg.norm(u)
print(norm_u)

norm_v=np.linalg.norm(v)
print(norm_v)
left=dot
right=norm_v+norm_u
if left<=right:
    print("Equality holds")
else:
    print("Equality not holds")
