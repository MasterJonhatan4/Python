"""BOOLEAN LOGIC"""

def AND (b1,b2):
    if b1 == "1" and b2 == "1":
        return "1"
    else:
        return "0"

    
def OR (b1,b2):
    if b1 == "1" or b2 == "1":
        return "1"
    else:
       return "0"


def XOR (b1,b2):
    if b1 != b2:
        return "1"
    else :
        return "0"
 
n = 4 # n is the lenght of the bits
b1 = "1111"
b2 = "0101"


b=""
for i in range (n):
    b += AND(b1[i],b2[i]) 
print(b1 + " AND " + b2 + " = " + b)

b= ""
for i in range (n):
    b += OR(b1[i],b2[i]) 
print(b1 + " OR " + b2 + " = " + b)

b=""
for i in range (n):
    b += XOR(b1[i],b2[i]) 
print(b1 + " XOR " + b2 + " = " + b)