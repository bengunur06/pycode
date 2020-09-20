from sys import argv
from os.path import exists

script , from_file , to_file = argv

print "Copying file %s to %s " % (from_file,to_file)

in_file = open(from_file)
indata= in_file.read()

print "Input file is %d bytes long " % len(indata)

print "Does the output file exsist ? %r" % exists(to_file)
print "Ready hit Return to continue , CTRL-C to abort "
raw_input()

out_file = open (to_file,'w')
out_file.write(indata)

print "All right all done "

out_file.close()
in_file.close()