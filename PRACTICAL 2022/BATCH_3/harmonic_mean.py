# Program to calculate the harmonic sum up to (n-1)

number = int(input("Enter the value of n: "))

harmonic_sum = 0

for i in range(1, number):
    harmonic_sum = harmonic_sum + (1 / i)

print("Harmonic sum up to", number - 1, "=", harmonic_sum)