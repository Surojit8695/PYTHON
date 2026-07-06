import numpy as np
u=np.array(list(map(int,input("Enter u vector:").split())))
v=np.array(list(map(int,input("Enter v vectir:").split())))

while True:
    print("----MENU----")
    print("1.Addition")
    print("2.Scalar multi")
    print("3.Dot")
    print("4.Cross")
    print("5.Orthogonality")
    print("6.Parallelism")
    print("7.Exit")
    choise=int(input("Enter your choise:"))
    if choise==1:
        print("Addition is:",u+v)
    elif choise==2:
        scalar=int(input("Enter the scalar value:"))
        print("Scalar multi for u is:",u*scalar)
        print("Scalar multi for v is:",v*scalar)
    elif choise==3:
        print("Dot product is:",np.dot(u,v))
    elif choise==4:
        print("Cross product is:",np.cross(u,v))
    elif choise==5:
        if np.dot(u,v)==0:
            print("This vectors are orthogonal")
        else:
            print("Not orthogonal")
    elif choise==6:
        if np.all(np.cross(u,v)==0):#np.cross() is designed mainly for 3D vectors.
            print("The vectors are parallel")
        else:
            print("The vectors are not parallel")
    elif choise==7:
        break
    else:
        print("Invalid input")


    
