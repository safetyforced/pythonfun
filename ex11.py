print "How old are you?",
age = raw_input()
print "How high are you?",
height = raw_input()
print "How heavy are you?",
weight = raw_input()

print "You're %r years old, %r tall, and weigh %r" % (age, height, weight)


print "\n enter a number",
num1 = int(raw_input()) #forces parse to int
print "enter another number",
num2 = input() #inteprets parsing
print "the sum is: %d" % (num1 + num2)
