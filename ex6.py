# create string to set up joke
x = "There are %d types of people." % 10

#make a string called "binary" with the value "binary"  you know, like you do
binary = "binary"

#create a string to enforce the use of contractions
do_not = "don't"

#create punchline string
y = "Those who know %s and those who %s." % (binary, do_not)

#print joke set up
print x

#print punchline
print y

#print unstyled string of joke set up
print 'I said: %r.' % x

#print styled string of punchline
print "I also said: '%s'." % y

#set boolean variable about the quality of the joke's humor to False
hilarious = False

#set string for determining joke funniness and call a... missing... variable...
joke_evaluation = "Isn't that joke so funny?! %r"

#This makes me very nervous
print joke_evaluation % hilarious

#set string with some words
w = "This is the left side of..."

#set string with different words
e = "a string with a right side."

#print the concatination of both strings
print w + e
