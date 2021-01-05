# A string S consisting of N characters is considered to be properly nested if any of the following conditions is true:

# S is empty;
# S has the form "(U)" or "[U]" or "{U}" where U is a properly nested string;
# S has the form "VW" where V and W are properly nested strings.
# For example, the string "{[()()]}" is properly nested but "([)()]" is not.

# Write a function:

# def solution(S)

# that, given a string S consisting of N characters, returns 1 if S is properly nested and 0 otherwise.

# For example, given S = "{[()()]}", the function should return 1 and given S = "([)()]", the function should return 0, as explained above.

# Write an efficient algorithm for the following assumptions:

# N is an integer within the range [0..200,000];
# string S consists only of the following characters: "(", "{", "[", "]", "}" and/or ")".
# Copyright 2009–2020 by Codility Limited. All Rights Reserved. Unauthorized copying, publication or disclosure prohibited.


def solution(S):
    nested = {'(': 1, ')': -1, '{': 2, '}': -2, '[': 3, ']': -3}
    nest = []
    for s in S:
        if nested[s] > 0:
            nest.append(s)
        if nested[s] < 0:
            if len(nest) == 0:
                return 0
            t = nest.pop()
            if abs(nested[t]) != abs(nested[s]):
                return 0
    if len(nest) != 0:
        return 0
    return 1
