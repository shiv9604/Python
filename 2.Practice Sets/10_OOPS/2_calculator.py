
class calculator:
    def __init__(self,num):
        self.number = num

    def square(self):
        print(f"the square of {self.number} is : {self.number **2}")

    def cube(self):
        print(f"the cube of {self.number} is : {self.number **3}")

    def squareRoot(self):
        print(f"the spuareRoot of {self.number} is : {self.number **0.5}")



a = calculator(2) # calling part 3 = num
b = calculator(8)
a.square()
a.cube()
b.squareRoot()