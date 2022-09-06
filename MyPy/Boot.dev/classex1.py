class Wall:
    armor = 10
    height = 5

    def fortify(self):
        print(self)
        self.armor *= 2


# -- TEST SUITE, DONT TOUCH BELOW THIS LINE --


def main():
    wall = Wall()
    print(wall.armor)
    print(wall.height)
    wall.fortify()
    print(wall.armor)
    print(wall.height)
    wall.fortify()
    print(wall.armor)
    print(wall.height)


main()
