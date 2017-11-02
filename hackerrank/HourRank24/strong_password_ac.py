#!/bin/python

import sys

def minimumNumber(n, password):
    numbers = "0123456789"
    lower_case = "abcdefghijklmnopqrstuvwxyz"
    upper_case = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    special_characters = "!@#$%^&*()-+"
    digitdiff = 6 - n
    componentdiff = sum(map(
        lambda x: 0 if set(password).intersection(set(x)) else 1,
        [numbers, lower_case, upper_case, special_characters]
    ))
    return max(digitdiff, componentdiff)

if __name__ == "__main__":
    n = int(raw_input().strip())
    password = raw_input().strip()
    answer = minimumNumber(n, password)
    print answer
