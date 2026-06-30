#complex number addition
class ComplexNumber:

    def __init__(self, real, img):
        self.real = real
        self.img = img

    def addCN(self, *nums):
        real_sum = self.real
        img_sum = self.img

        for i in nums:
            real_sum += i.real
            img_sum += i.img

        print("Sum =", real_sum, "+", img_sum, "i")


n = int(input("Enter the number of complex numbers: "))

obj = []

for i in range(n):
    real = int(input("Enter real part: "))
    img = int(input("Enter imaginary part: "))
    obj.append(ComplexNumber(real, img))

obj[0].addCN(*obj[1:])