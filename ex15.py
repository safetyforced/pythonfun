# imports argv module from sys
from sys import argv

# set the variables according to passed arguments using argv module
script, filename = argv

# use open to return a file object
txt = open(filename)

# print stuff
print "Here's %r:" % filename

# print the output of the read function on file object
print txt.read()

# # print stuff
# print "Type the filename again:"
#
# # user input is stored in variable
# file_again = raw_input("> ")
#
# # file object is returned
# txt_again = open(file_again)
#
# # print the output of the file
# print txt_again.read()
