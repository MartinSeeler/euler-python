sum_of_even = 0
prev = 0
current = 1
next = current
while (prev+current) <= 4000000:
    next = prev + current
    prev = current
    current = next
    if next % 2 == 0:
        sum_of_even += next



print "The sum of all even is %s" % sum_of_even


