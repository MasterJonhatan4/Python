"""BOOLEAN LOGIC"""
#The purpose of this program is to illustrate fundamental propositional logic functions like AND, OR, and XOR. 


def AND(b1,b2,b):
    if b1 and b2 == "1":
        b = "1"
    else:
        b = "0"
    print (b1 + " AND " + b2 + " = " + b)
    

def OR (b1,b2,b):
    if b1 or b2 == "1":
        b = "1"
    else:
        b = "0"
    print (b1 + " OR " + b2 + " = " + b)
    
    

def XOR (b1,b2,b):
    if b1 != b2:
        b = "1"
    else :
        b = "0"
    print (b1 + " XOR " + b2 + " = " + b)
   

b1 = "1" 
b2 = "1"
b = ""

AND(b1,b2,b)

OR(b1,b2,b)

XOR(b1,b2,b)
