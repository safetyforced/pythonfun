from sys import argv

script, user_name, user_age = argv
prompt = 'input hurr: '

print "Hi %s I'm the script %s" % (user_name,script)
print "I'd like to ask you a few questions"
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print """
Alrighty, so you said %r to liking me
you live in %r.  Nice place.
and you compute on a %r.  Neat.
also you are %s years old
""" % (likes, lives, computer, user_age)
