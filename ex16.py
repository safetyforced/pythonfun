from sys import argv

script, filename = argv

print "We gon erase %r" % filename
print "If that's SUPER BAD control-c stat"
print "if'n ya wanna, hit return"

raw_input("?")

print "Opening..."
target = open(filename, 'w')

print "Truncating/DELETING..."
target.truncate()

print "Write your own stuff:"

line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "Writing..."
ln = "\n"

target.write(line1 + ln + line2 + ln + line3 + ln)

print "Closing/saving..."
target.close()
