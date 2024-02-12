def main (): 
    
    final = int(input ("insert the final value: "))
    initial = int(input("insert the initial value: "))
    decrease(initial, final)
    
    


def decrease (value, limit):
    if value <= limit: 
        print(value)
        decrease(value + 1, limit)
        
    else: 
        return 0
        
        
        

a = main()