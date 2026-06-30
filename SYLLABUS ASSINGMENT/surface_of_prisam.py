#Write a program that takes the lengths of the three sides of a prism as input (integers) and
#computes its surface area using the formula: 2ab + 2bc + 2ca.
a = int(input("Enter the side a of the prism: "))
b = int(input("Enter the side b of the prism: "))
c = int(input("Enter the side c of the prism: "))
surface=2*a*b + 2*b*c + 2*c*a
print("The surface area of the prism is:", surface)
