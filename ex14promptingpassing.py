from sys import argv

script, user_name = argv

prompt = '> '

print "Hi %s I'm the %s script ." % ( user_name,script)
print "I would like to ask few questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s ?" % user_name
lives = raw_input(prompt)

print "what kind of a computer do you have ?"
computer = raw_input(prompt)

print """
Alright so you said %r about liking me 
You live in %r not sure where that is 
And you have a %r computer nice 
"""% (likes,lives,computer)