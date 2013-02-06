#!/usr/bin/env python

### HOMEWORK ASSIGNMENT NUMBER ONE
# This introduces functions which are defined by the keyword 'def'
# in the form of 'def functionname(args):' where args are the arguments
# passed to the function. If we wanted to make a function named adder
# that took in two numbers named x and y, it would have the function signature of
# 'def adder(x, y): ' The colon after the arguments is VERY important
# as it lets Python know that it is the start of a block of code. A block
# is indicated by indention. Every line that belongs to a function will be indented.
# You return things from functions with, you guessed it, the return keyword.
# if I wanted to add together and return the two values from adder, x and y,
# I would use the statement 'return x + y'. Don't worry, we'll go over
# functions in GREAT detail later on, so don't panic if you're confused.

# Your assignment is to fill in the code for the functions provided.
# The functions have already been defined, for example:

### def example(x, y):
###     # your code here
###     return


# If your task was to return the result of multiplying arguments of
# the example(), the values x and y, your solution may look like:

### def example(x, y):
###     return x * y

# or it could look like:

### def example(x, y):
###     result = x * y
###     return result



### QUESTION ONE
# Given an arbitrary amount of apples as an integer,
# return back a string "Number of Apples: <count>"
# where <count> is the variable being passed in.
# The string formatting has to be exact, including spaces.
# So, question1(5) would return 'Number of Apples: 5'
def question1(count):
    
    return "Number of Apples: {count}".format(count=count)




### QUESTION TWO
# Given a persons name as the string person_name,
# return back a string that greets the person in the form of
# "Hello <person_name>, your name is <num> characters long"
# where num is the length of the string person_name.
# That means question2('John') would yield a value of
# "Hello John, your name is 4 characters long"
def question2(person_name):
    name_len = len(person_name)
    return "Hello {person_name}, your name is {name_len} characters long".format(person_name=person_name, name_len=name_len)





### QUESTION THREE
# Given two lists named list_one and list_two,
# return a new list that consists of the first
# three elements of list_one followed by the
# last element of list two. remember that you
# use [] to index things. Eg, my_var[num].
def question3(list_one, list_two):
    # your code here
    return





### QUESTION FOUR
# Given an arbitrary value x (int or float), return
# a list consisting of x^2, x^3, x^4, x^5. That means
# a call of question4(3) should return [9, 27, 81, 243]
def question4(x):
    # your code here
    return





### QUESTION FIVE
# Given two strings, str_one and str_two, return the
# first three characters of str_one concatenated with
# (added to) the first three characters of str_two such
# that question5('Brad', 'Trent') will produce 'BraTre'3
# Hint: You can index strings just like you index lists.
# Extra credit: look up "slicing" and use that to solve
# this problem and question three.
def question5(str_one, str_two):
    # your code here
    return




##############################################################################################
##############################################################################################
##############################################################################################
##############################################################################################









from collections import namedtuple, Iterable

def main():
    Test = namedtuple('Test', ['Func', 'Args', 'Answer'])

    tests = [Test(Func=question1,
                  Args=5,
                  Answer='Number of Apples: 5'),
             Test(Func=question1,
                  Args=27,
                  Answer='Number of Apples: 27'),
             Test(Func=question1,
                  Args=0,
                  Answer='Number of Apples: 0'),
             Test(Func=question2,
                  Args='John',
                  Answer='Hello John, your name is 4 characters long'),
             Test(Func=question2,
                  Args='ReallyLongFakeName',
                  Answer='Hello ReallyLongFakeName, your name is 18 characters long'),
             Test(Func=question2,
                  Args='King of Sweden',
                  Answer='Hello King of Sweden, your name is 14 characters long'),
             Test(Func=question3,
                  Args=([1, 2, 3, 4, 5], [6, 7, 8, 9]),
                  Answer=[1, 2, 3, 9]),
             Test(Func=question3,
                  Args=([7, 1, 4], [8]),
                  Answer=[7, 1, 4, 8]),
             Test(Func=question3,
                  Args=([None, 'Dog', 2.9, {'a', 'b'}], [False, True, True]),
                  Answer=[None, 'Dog', 2.9, True]),
             Test(Func=question4,
                  Args=3,
                  Answer=[9, 27, 81, 243]),
             Test(Func=question4,
                  Args=-5,
                  Answer=[25, -125, 625, -3125]),
             Test(Func=question4,
                  Args=10,
                  Answer=[100, 1000, 10000, 100000]),
             Test(Func=question5,
                  Args=('Brad', 'Trent'),
                  Answer='BraTre'),
             Test(Func=question5,
                  Args=('015394', '1894375'),
                  Answer='015189'),
             Test(Func=question5,
                  Args=('number one', 'in the hood, g'),
                  Answer='numin ')]

    for i, test in enumerate(tests):
        if isinstance(test.Args, Iterable) and not isinstance(test.Args, basestring):
            res = test.Func(*test.Args)
        else:
            res = test.Func(test.Args)

        if res == test.Answer:
            status = 'PASS'
        else:
            status = 'FAIL'

        print "{0}: {1} {2} -- got: {3}, expected: {4}\n".format(i, test.Func.__name__,
                                                                 status, res, repr(test.Answer))

if __name__ == '__main__':
    main()
