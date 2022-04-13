import os

import ps4_controller


axis_data = None
button_data = None
hat_data = None


if __name__ == "__main__":
    ps4 = ps4_controller.PS4Controller()
    while True:
        axis_data, button_data, hat_data = ps4.listen()
        print(axis_data)
        print(button_data)
        print(hat_data)
        os.system('cls')
