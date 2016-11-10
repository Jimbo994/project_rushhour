class Vehicle(object):
    def __init__(self, id, x, y, orientation):
        self.id = id
        self.length = 2

        self.x = x
        self.y = y

        if orientation == 'H':
            self.orientation = orientation
            x_end = self.x + (self.length - 1)
            y_end = self.y
        elif orientation == 'V':
            self.orientation = orientation
            x_end = self.x
            y_end = self.y + (self.length - 1)

    def vehicleInfo(self):
        return "Vehicle({0}, {1}, {2}, {3})".format(self.id, self.x, self.y, self.orientation)

# class VehicleHorizontal(Vehicle):
#     def __init__(self, id, x, y):
#         self.id = id
#         self.x = x
#         self.y = y
#     def getCarPosition(self):
#         return self.pos
