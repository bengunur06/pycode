def cheese_and_crackers(cheese_count , boxes_of_crackers ):
    print "you have %d cheeses !" % cheese_count
    print  "you have %d boxes of crackers !" % boxes_of_crackers
    print "Man that's enough for a party !"
    print "Get a blanket . \n "



print "We can just give the function numbers directly :"
cheese_and_crackers(20,30)

print "or we can use variables from our script "
amount_cheese = 10 
amount_cracker = 50

cheese_and_crackers(amount_cheese,amount_cracker)

print "We can even do the math inside too !"
cheese_and_crackers(10+5,80+30)

print "We can combine two variable and math "
cheese_and_crackers(amount_cheese+20,amount_cracker+90)