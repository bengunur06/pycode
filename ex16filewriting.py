from sys import argv

script , filename = argv

print "WE are going to erase %r" % filename
print "if you dont want that hit CTRL-C (^C)"
print "If you do want that hit Return "
raw_input("?")

print "opening file ..."
target = open(filename,'w')

print "Turnicating the file day Goodbye ! "
target.truncate()

print " Now i am going to ask you for 3 lines "
line1 = raw_input("line1:")
line2 = raw_input("line2:")
line3 = raw_input("line3:")

print "I am going to write the to the file "

target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)

print " and we close it here "

target.close()