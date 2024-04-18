#Samantha Patin and Sydney Eidelbes

class Fabric:
    def __init__ (self, countryOfOrigin, color):
        self.countryOfOrigin=countryOfOrigin
        self.color=color
    def __str__(self):
        return self.countryOfOrigin+"("+str(self.color)+")"

shirt=Fabric("Canada", "Blue")

print(shirt)
