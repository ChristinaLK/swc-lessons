#Python lesson notes

##Intro

Move everyone into the python directory.  Create a hello_world.py script and run.  

Doing the same thing as this morning - writing more complex things to solve questions.  

This morning we learned about using the shell to manage files and run programs on our computer.  
That is, we were dealing with different types of "file" objects (text files, data files, etc.)
- think of these as 'nouns' - and various commands to manipulate them - sort of like verbs.
What we're going to do this afternoon is similar, but instead of using files + shell commands, 
we'll be creating 'object-nouns' and 'program-verbs' all within the python language.  

> Have everyone import numpy right away to make sure it's installed properly.  
> Then it can be fixed while you do the first part of the lecture.  

##Ipython Orientation

In no particular order

1. How to run cells
2. How to add cells
3. NOT online
4. Accessing help (question mark)
5. tab completion

##Nouns

Just like there are all kinds of file types on your computer, we can create several 
different types of objects in python.  

1. Numbers: basic computations, floats vs ints
2. Strings: concatentate
3. Lists: talk about slicing (go back and mention lists)
4. Dictionaries: fancier lists, how to add elements

Python decides for you what the variable type will be.  You can force the variable 
assignment (called "casting").  

> Do exercises (type issues, slicing, concatenating strings, etc.)

##Verbs

###Methods

One of the features of different types of variables are built in "methods".  
You can access the methods for a certain type by typing out the variable name, 
then a period, the method name, and parentheses with possible arguments.  

1. Lists: append, extend, pop, etc.
2. Dictionaries: keys, values
3. Strings

~~~
lotto_numbers = lotto_numbers.strip()

print lotto_numbers.split(',')

print answer.replace('=', '').replace('&', 'e').replace('~', 'o').replace('!', ' ')
~~~

###Functions

What if we want to write our own function?  Diagram anatomy of function:

~~~
name(arguments):
	process
	return
~~~

Talk about indenting, etc.  Give following 4 examples

*no arg/no return: hello world

*arg/no return: print nice message

*arg / return: initials

> previous one as exercise

Talk about default values

~~~
def calculate_gc(x):
    """Calculates the GC content of DNA sequence x.
    x: a string composed only of A's, T's, G's, and C's."""
    x = x.upper()
    gc = (x.count('C') + x.count('G'))/float(len(x))
    return gc
~~~

Talk about documenting code with comments

Segue into numpy

##Logic and Flow Control

###For Loops


###If/Then Statements

~~~
x = 5
if x < 0:
    print "x is negative"
else:
    print "x in non-negative"
~~~


##Scripting in the Shell

~~~
import sys

print 'version is', sys.version
print 'arguments are', sys.argv
~~~




