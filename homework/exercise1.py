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
    # your code here
    return





### QUESTION TWO
# Given a persons name as the string person_name,
# return back a string that greets the person in the form of
# "Hello <person_name>, your name is <num> characters long"
# where num is the length of the string person_name.
# That means question2('John') would yield a value of
# "Hello John, your name is 4 characters long"
def question2(person_name):
    # your code here
    return





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





###############################################
####                                       ####
####             !!! ALERT !!!             ####
####                                       ####
###############################################
## The testing function lays below. Typically we would use something called
## a unit testing library to test all our problems, but I opted to roll my own
## tests so you could see some more Python in action if you felt like looking.
## Later assignments may or may not use to a proper unit testing library
## depending on how lazy I feel on that particular day.




# We are importing the objects namedtuple and Iterable from the module collections.
# This is code that is part of the Python Standard Library that someone else has written
# for our benefit. I could have also imported these with a so-called regular import like:
# 'import collections' and then any time I needed to refer to namedtuple I could type
# collections.namedtuple, but I opted to just directly import the objects I needed.
from collections import namedtuple, Iterable

def main():
    # Namedtuple allows us to create a simple data structure that contains
    # the fields we specify so that they can be accessed by Namedtuple.field
    # or through regular indexing operations like Namedtuple[0].
    Test = namedtuple('Test', ['Func', 'Args', 'Answer'])


    # We then create a list of our namedtuple, named Test, that will
    # contain the function we want to test, some arguments to test
    # it with, and the expected output from that function. Note that you
    # do not have to format things this way syntactically, it's merely stylistic.
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

    # Now iterate through our list of Tests, but count each iteration and
    # return the current count along with the Test for that particular
    # iteration via the built-in function enumerate(), starting with 0.

    # Note that word 'test' in our for loop is different from the namedtuple
    # that called Test. Python is case-sensitive, so be careful with naming.
    for i, test in enumerate(tests):

        # Here we check if test.Args is an iterable, which includes lists, tuples,
        # dictionaries, and strings. We do not however, want our check to pass if
        # test.Args is a regular string, as opposed to some other type of iterable.
        if isinstance(test.Args, Iterable) and not isinstance(test.Args, basestring):

            # If our check passed then we call the function in the test,
            # with the arguments provided. But we call it with the asterisk or *
            # operator. The * does a lot of stuff in Python (and a lot of other
            # languages!), but here it "unpacks" our arguments. Assuming a = [3, 2],
            # the function call example(a) would actually be example([3,2]) which would
            # be a problem if example expected two intss as arguments instead of a list.
            # example(*a), however, would expand the list to produce example(3, 2)
            res = test.Func(*test.Args)
        else:
            # call our function, but don't try to expand our arguments, as
            # it would throw an exception (error) if it wasn't an iterable.
            res = test.Func(test.Args)

        # now we just test to see if the results of our test match our expectations.
        if res == test.Answer:
            status = 'PASS'
        else:
            status = 'FAIL'

        # and print it all out. __name__ is a special attribute that "callables" such
        # as functions and classes have that tells you the name of the callable. In this
        # case, it returns our function names, eg question1, question2, etc.

        # repr() is a built-in function that returns the representation of an object, which
        # can be different from calling str() on that object. We use it here because we want
        # our strings to show their quotation marks since some of our tests have spaces in them.
        print "{0}: {1} {2} -- got: {3}, expected: {4}\n".format(i, test.Func.__name__, status,
                                                                 repr(res), repr(test.Answer))


# Standard Python boilerplate code. All it means is we run the function main() ONLY
# if this file is being ran directly, but not if it has been imported by another file.
# The reason we do this is because Python needs something not in a class or function
# to start our program with, such as a call to a function, such as main(). However,
# if we didn't have our if statement and just had a call to main(), any time someone
# imported our file our code would automatically run, regardless of whether they wanted
# it to or not. You can imagine how that could cause a clusterfuck of biblical proportions.
if __name__ == '__main__':
    main()
