# create function that prints the input arguments
def cheese_and_crackers(cheese_count, box_of_crackers):
    print "You have %d cheese!" % cheese_count
    print "You have %d boxes of crackers" % box_of_crackers
    print "That's awesome!\n"

# print arguments using static values
print "We can just give the function number directly:"
cheese_and_crackers(20, 30)

# arbitrarily set variable values
print "OR we an use variables from the script:"
amount_of_crackers = 50
amount_of_cheese = 10

# print arguments using variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# ditto using math arguments
print "We can even do math, too:"
cheese_and_crackers(10 + 20, 5 + 6)


# variables plus math!  look out!
print "And we can combine the two, variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
