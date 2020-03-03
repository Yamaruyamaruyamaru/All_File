#cubed

def function(val:int):
    try:
        num =int(val)
    except:# NameError:
        print("Invalid Value.Enter number")
        
    print("num**3",num**3)
    
