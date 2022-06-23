class Road:
    def __init__(self):
        self._road_lenght = int()
        self._road_width = int()

    def asphalt_canvas(self, road_lenght, road_width):
        mass_of_canvas_m3 = int(25)
        thickness_of_canvas = int(5)
        return road_lenght * road_width * mass_of_canvas_m3 * thickness_of_canvas


road_1 = Road()
print(f'Масса асфальта, необходимого для покрытия всей дороги: {road_1.asphalt_canvas(1000, 15)}')
