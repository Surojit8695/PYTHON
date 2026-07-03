class Animal:

    def sound(self):
        print("Animals make sound")


class Dog(Animal):

    def bark(self):
        print("Dog Barks")


class Cat(Animal):

    def meow(self):
        print("Cat Meows")


print("\n========== HIERARCHICAL INHERITANCE ==========")

d = Dog()
d.sound()
d.bark()

print()

cat = Cat()
cat.sound()
cat.meow()