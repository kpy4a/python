import time


class TrafficLight:

    def __init__(self, colors):
        self.__colors = colors

    __color = ""
    __colors = dict()

    def running(self):
        i = 0
        while True:
            color_object = self.__colors[i % len(self.__colors)]
            self.set_color(color_object["name"])
            time.sleep(color_object["timeout"])
            i += 1

    def set_color(self, color):
        print(f"New color: {color}")
        self.__color = color


traffic = TrafficLight({
    0: {
        "name": "red",
        "timeout": 7
    },
    1: {
        "name": "yellow",
        "timeout": 2
    },
    2: {
        "name": "green",
        "timeout": 5
    }
})
traffic.running()
