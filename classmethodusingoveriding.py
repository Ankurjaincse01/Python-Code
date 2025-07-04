class MO1: # Parent Class
    def myFunction(self,a):
        print("Class MO1 function Called")
        
class MO2(MO1): # Child Class
    def myFunction(self,a):
        print("Class MO2 function called")
        # Super method calling the method of class MO1
        super().myFunction(10)
        
class MO3(MO2): # Child Class
    def myFunction(self,a):
        print("Class MO3 function called")
        # Super method calling the method of class MO2
        super().myFunction(10)
        
# Creating an object of class MO3
m = MO3() # Object of MO3
m.myFunction(10)