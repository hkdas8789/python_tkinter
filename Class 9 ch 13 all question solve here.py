
class surface_area_volume:
    pi=3.142857142857143
    def __init__(self,name):
        self.Name=name

    def csa_Cylinder(self,unit):
        try:# 2*pi*r*h
            r=float(input("Enter radius\t:-\t"))
            h=float(input("Enter height\t:-\t"))
            return(f"C.S.A of {self.Name} is {2*surface_area_volume.pi*r*h} {unit} square .")
        except Exception as e:
            print(e)
    def tsa_Cylinder(self,unit):
        try:# 2*pi*r*h + 2pi*r**2
            r=float(input("Enter radius\t:-\t"))
            h = float(input("Enter height\t:-\t"))
            return (f"T.S.A of {self.Name} is {2*self.pi*r*h + 2*self.pi*r*r} {unit} square .")
        except Exception as ee:
            print(ee)
    def volume_Cylinder(self,unit):
        try:# V = πr2h
            r=float(input("Enter radius\t:-\t"))
            h = float(input("Enter height\t:-\t"))
            return (f"Volume of {self.Name} is {surface_area_volume.pi*r*r*h} {unit} cube .")
        except Exception as e:
            print(e)
class physics(surface_area_volume):
    pass

cy=surface_area_volume("Cylinder")
print(cy.volume_Cylinder("meter"))


#r - 2.1 m , h - 4.5
# tsa is 87.12
# csa is 59.4


