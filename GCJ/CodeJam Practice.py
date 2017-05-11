
# coding: utf-8

# CodeJam Practice

# In[23]:

def last_number(orig_number):
    curr_number = 0
    digit_appeared = [False] * 10
    while sum(digit_appeared) < 10:
        curr_number += orig_number
        numcheck = curr_number
        while numcheck > 0:
            digit_appeared[numcheck % 10] = True
            numcheck /= 10
        
    return curr_number


# In[28]:

t = int(raw_input())  # read a line with a single integer
for i in xrange(1, t + 1):
    a = int(raw_input()) 
    if a == 0:
        print("Case #%d: INSOMNIA" % (i))
        continue
    print("Case #%d: %d" % (i, last_number(a)))

