formatter = "%r %r %r %r"

print formatter % (1,2,3,4)
print formatter % ("one","two","three","four")
print formatter % (True, False, False, True)
print formatter % (formatter, '%r %r %r %r', formatter, formatter)
print formatter % (
    "I had this thing.",
    "I'm not writing more poetry.",
    "A haiku:",
    "Just Kidding."
)

# watch your modulusseseeses
# write more poetry
# my quotes were different. Maybe the string length?
