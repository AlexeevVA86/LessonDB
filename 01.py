import time
import os


def clear(): return os.system('cls' if os.name == 'nt' else 'clear')


class TrafficLight:
    __color = ['Red', 'yellow', 'Green']

    def running():
        print(TrafficLight.__color[0])
        while True:
            clear()
            print(TrafficLight.__color[0])
            time.sleep(7)
            clear()
            print(TrafficLight.__color[1])
            time.sleep(2)
            clear()
            print(TrafficLight.__color[2])
            time.sleep(4)


TrafficLight.running()
