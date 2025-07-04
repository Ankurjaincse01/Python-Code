class RBI: # Abtract Class
    def Interest(self): # Abs
        pass
    
class SBI(RBI): # Child Class
    def Interest(self): # RBI Interest Implements here
        print("SBI Interest is 5%")
        
class HDFC(RBI): # Child Class
    def Interest(self): # RBI Interest Implements here
        print("HDFC Interest is 2%")
s = SBI()
h = HDFC()
s.Interest() 
h.Interest() 
