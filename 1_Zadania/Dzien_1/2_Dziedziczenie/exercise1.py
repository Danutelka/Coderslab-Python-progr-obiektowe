class Dinosaur:

    def walk(self):
        return "Chodzę!"

    def make_sound(self):
        return "Roar!"


if __name__ == "__main__":
    d = Dinosaur()
    print("Dinozaur chodzi:")
    print(d.walk())

    print("Dinozaur wydaje dźwięk:")
    print(d.make_sound())
