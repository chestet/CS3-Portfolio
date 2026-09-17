class Glassware:                            # Parent Class
    def __init__(self):
        self.glassware = Glassware
        
class Beaker(Glassware):                    # Child Class    
    def __init__(self):
        super().__init__()
        self.beaker = Beaker
        print("Beaker is created")

class Tray:                                 
    def __init__(self):
        print("Tray is created")
        self.tray = []                      # Tray without beakers yet
        for i in range (5):
            self.tray.append(Beaker())      # Creating and appending the beaker to the tray
    def __del__(self):
        print("Tray has been deleted")
        del self.tray                       # Deleting the tray therefore voiding the 5 beakers in it
        for i in range(5):
            print("Beaker has been deleted")
            
glass = Tray()
del glass
