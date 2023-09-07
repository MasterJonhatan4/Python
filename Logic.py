"""LOGIC"""

def neg (p):
    return  not p


def conj(p,q):
    if p == True and q == True:
        return True
    else:
        return False
    

def disj (p,q):
    if p == True or q == True:
        return True
    else:
        return False
    
def impl (p,q):
    if p == True and q == False:
        return False
    else:
        return True
    

def equi(p,q):
    if p == q :
        return True
    else:
        return False


def exdisj(p,q):
    if p == q:
        return False
    else:
        return True

p = False #Input directly the truth value you want to test 
q = False #Input directly the truth value you want to test 
print("p= " + str (p) )
print("q= " + str (q) )

#The part below is optionnal.
print("conj (p,q) = " + str(conj(p,q)))
print("disj (p,q) = " + str(disj (p,q)))
print("impl (p,q) = "+ str(impl (p,q)))
print("equi(p,q) = " + str(equi(p,q)))
print()
print("exdisj(p,q) = " + str(exdisj(p,q)))
