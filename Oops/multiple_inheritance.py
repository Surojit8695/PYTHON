class Sports:

    def sports(self):
        print("Plays Cricket")


class Music:

    def music(self):
        print("Loves Music")


class AllRounder(Sports, Music):

    def intro(self):
        print("I am an All Rounder Student")


print("\n========== MULTIPLE INHERITANCE ==========")

a = AllRounder()

a.intro()
a.sports()
a.music()
