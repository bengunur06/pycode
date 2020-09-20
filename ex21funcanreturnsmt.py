def add(a , b):
    print  "Adding %d + %d " % (a,b)
    return a+b


def substract(a , b ):
    print "Substracting %d and %d " % (a,b)
    return a-b

def divide(a , b ):
    print "Dividing %d and %d " % (a,b)
    return a/b



print "Lets do something with functions "

age = add(19,1)
height= substract(190,15)
weight = add(70,5)

print " So the age is :%d \n Height is :%d \n Weight is :%d \n " % (age,height,weight)