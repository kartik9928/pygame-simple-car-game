from obstacle_car import cars_creation

class Right_cars(cars_creation):

    def __init__(self):
        car_x_co = [336, 443, 347, 446]
        car_speed = 1
        super().__init__(car_x_co, car_speed)