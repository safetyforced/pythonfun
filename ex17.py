from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

# I guess I'll just do this on one line
indata = open(from_file).read()
# indata = in_file.read()

print "the file is %d bytes long" % len(indata)
print "Does the output file exist? %r" % exists(to_file)
print "Enter to continue, CTRL-C to abort"
raw_input()

out_file = open(to_file, 'w')
out_file.write(indata)
out_file.close()

print "DONE!"
