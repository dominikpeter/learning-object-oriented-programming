from __future__ import print_function

class Coffee(object):
    def __init__(self, size):
        self.sizes = ['S', 'M', 'L', 'XL']
        assert size.upper() in self.sizes
        self._size = size
        self.isEmpty = True
        self.beans = None

        print("You got a {} sized coffee cup".format(self._size))

    @property
    def size(self):
        print("You got a {} sized coffee".format(self._size))
        return self._size

    @size.setter
    def size(self, newsize='M'):
        try:
            if newsize.upper() not in self.sizes:
                print("New cup size does not exist, keeping old one")
                newsize = self._size
            elif self.isEmpty:
                print("Getting a new cup of size {}".format(newsize.upper()))
            elif sizes.index(newsize) < sizes.index(self.size):
                print('You cannot fill your coffee into a smaller cup')
                print("Keeping your old cup size.")
                newsize = self._size
            else:
                print('Filling your coffee in a new cup with size {}')
        except IndexError:
            print("Size does not exist. Kepping old size")
            newsize = self._size
        self._size = newsize

    def fill(self, beans='Arabica'):
        if self.isEmpty:
            self.beans = beans
            print('Filling coffee with rosted "{}" beans'.format(self.beans))
            self.isEmpty = False
        else:
            print("Your coffee is already filled")

    def drink(self):
        if self.isEmpty:
            print("""Your Coffee is empty.
            You have to fill it before you can drink""")
        else:
            print("Mhhhh it tasts sooo goood!!!")
            self.isEmpty = True


def main():
    coffee = Coffee('M')
    coffee.size = 's'

    coffee.fill('Black Arabica')
    coffee.drink()
    coffee.size = 'XL'
    coffee.fill('Africa')
    coffee.size = 'S'

    size = coffee.size

    coffee2 = Coffee(size)


if __name__ == "__main__":
    main()
