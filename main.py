import ps4_controller as ps4


import os

class Omni_wheel:
    def __init__(self):
        self.axis_data = None
        self.button_data = None
        self.hat_data = None
        self.controller = ps

    def move(self):
        while True:
            self.axis_data, self.button_data, self.hat_data = self.controller.listen()
            Vx = self.axis_data[0]
            Vy = self.axis_data[1]
            V1 = Vx
            V2 = Vy * -1
            V3 = Vx * -1
            V4 = Vy




if __name__ == "__main__":
    ps4 = ps4_controller.PS4Controller()
    while True:
        axis_data, button_data, hat_data = ps4.listen()
        print(axis_data)
        print(button_data)
        print(hat_data)
        os.system('cls')
