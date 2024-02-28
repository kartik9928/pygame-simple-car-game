from obstacle_car import cars_creation

class Left_cars(cars_creation):

    def __init__(self):
        car_x_co = [148, 174, 230, 270, 148, 174]
        car_speed = 10
        super().__init__(car_x_co, car_speed)