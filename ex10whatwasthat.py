tbyct = "\tI'm tabbed in."
prsct = "I'm split\non a line "
bckslshct = "I \\ am \\ a \\ cat "

fat_cat = """
I'll do a list : 
\t* Cat food
\t* Fish
\t* Catnip\n\t* Grass 
"""

print tbyct
print prsct
print bckslshct
print fat_cat

while True:
    for i in ["/","- ","|","\\","|"]:
        print "%s\r" % i,