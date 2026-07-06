import numpy as np
from sympy import Matrix
row1=int(input("Enter the number of row:"))
col1=int(input("Enter the number of col:"))
A=[]
print("\nEnter A matrix(NxN)")
for i in range(row1):
    u=list(map(int,input().split()))
    A.append(u)

A=np.array(A)
print(A)
print(type(A))

while True:
    print("----MENU----")
    print("1.Determinant")
    print("2.Inverse")
    print("3.Transpose")
    print("4.Scalar mult")
    print("5.Adjoint")
    print("6.Rank")
    print("7.Diagonal")
    print("8.Trace")
    print("9.Eigenvalue")
    print("10.Eigenvector")
    print("11.Ext+it")
    choise=int(input("Enter your choise:"))
    if choise==1:
        print("Determinant is:",np.linalg.det(A))
    elif choise==2:
        print("Inverse is:",np.linalg.inv(A))
    elif choise==3:
        print("Transpose is:",A.T)
    elif choise==4:
        scalar=int(input("Enter the scalar value:"))
        print("Scalar mul is:",scalar*A)
    elif choise==5:
        B=Matrix(A)
        print("Adjoint of A is:",B.adjugate())
    elif choise==6:
        B=Matrix(A)
        print("Rank of A is:",B.rank())
    elif choise==7:
        B=Matrix(A)
        print("Diag element are:",B.diagonal())
    elif choise==8:
        B=Matrix(A)
        print("Trace of A is:",B.trace())
    elif choise==9:
        value,vector=np.linalg.eig(A)
        print("Eigenvalue of A is:",value)
    elif choise==10:
        value,vector=np.linalg.eig(A)
        print("Eigenvector of A is:",vector)
    elif choise==11:
        break
    else:
        print("Invalid input")
