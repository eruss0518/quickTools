class conv:
    def unitOf(self, num, unit):
        
        if unit == 1:
            
            num2 = num / 125.0
            
            #num3 = round(num2, 5)
            print(num2)
            #print(num3)
            num4 = (num2 * 60.0)
            final_num = round(num4, 2)

            return final_num
        
        elif unit == 2:
            


            num2 = num / 125000
            num3 = round(num2, 8)
            num4 = (num3 * 60.0) * 60.0
            final_num = round(num4, 2)

            return final_num
        else:
            f = str("Didnt work")
        
            return f
def method():
    print("conv")