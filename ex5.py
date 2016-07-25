name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'

print "My name is %s." % name
print "I am %s inches tall." % height
print "You could also think of me as %s feet, %s inches tall." % (height / 12, height % 12)
print "I weigh %s pounds." % weight
print "I have %s eyes and %s hair" % (eyes, hair)
print "Thankfully, my teeth are %s." % teeth

print "if I add %d, %d and %d I get %d" % (age, height, weight, age + height + weight)
