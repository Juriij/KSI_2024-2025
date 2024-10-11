# pomocna funkce
def pretty_print(igloo):
    return "radius: " + str(igloo.radius) + "\nInhabitants: " + str(igloo.inhabitants)

# Tady definujte tridu Igloo
class Igloo:
    def __init__(self, radius):
        self.radius = radius
        self.inhabitants = 0
        