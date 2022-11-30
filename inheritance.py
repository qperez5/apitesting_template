global_var = 2

class Vehicle:

    def start_engine(self):
        print('Engine started!')


class Car(Vehicle):

    def start(self):
        self.start_engine()  # definido en la clase padre
        print('Vroom Vroom')


car = Car()
car.start()
car.start_engine()

print(globals())
