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

In order to load our inflammation data, we need to import a library called NumPy that knows how to operate on matrices:

	import numpy

Importing a library is like getting a piece of lab equipment out of a storage locker and setting it up on the bench. Once it's done, we can ask the library to read our data file for us:

	numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')


Just like there are all kinds of file types on your computer, we can create several 
different types of objects in python.  

1. Numbers: basic computations (do conversion, bmi calculation), floats vs ints
2. Strings: concatentate
3. Lists: talk about slicing (go back and mention lists)
4. Dictionaries: fancier lists, how to add elements

Python decides for you what the variable type will be.  You can force the variable 
assignment (called "casting").  

> Do exercises (type issues, slicing, concatenating strings, etc.)

Back to numpy

	data = numpy.loadtxt(fname='inflammation-01.csv', delimiter=',')

	This statement doesn't produce any output because assignment doesn't display anything. If we want to check that our data has been loaded, we can print the variable's value:

	print data

	print type(data)
	
	<type 'numpy.ndarray'>

The output tells us that data currently refers to an N-dimensional array created by the NumPy library. We can see what its shape is like this:

	print data.shape

This tells us that data has 60 rows and 40 columns. data.shape is a member of data, i.e., a value that is stored as part of a larger value. We use the same dotted notation for the members of values that we use for the functions in libraries because they have the same part-and-whole relationship.

If we want to get a single value from the matrix, we must provide an index in square brackets, just as we do in math:

	print 'first value in data:', data[0, 0]

##Verbs

###Methods

One of the features of different types of variables are built in "methods".  
You can access the methods for a certain type by typing out the variable name, 
then a period, the method name, and parentheses with possible arguments.  We've already seen this with loadtxt.  

1. Lists: append, extend, pop, etc.
2. Dictionaries: keys, values
3. Strings

~~~
lotto_numbers = lotto_numbers.strip()

print lotto_numbers.split(',')

print answer.replace('=', '').replace('&', 'e').replace('~', 'o').replace('!', ' ')
~~~

Return to numpy page.  

Arrays also know how to perform common mathematical operations on their values. If we want to find the average inflammation for all patients on all days, for example, we can just ask the array for its mean value

	print data.mean()

NumPy arrays have lots of useful methods:

	print 'maximum inflammation:', data.max()
	
	print 'minimum inflammation:', data.min()
	
	print 'standard deviation:', data.std()
	

	patient_0 = data[0, :] # 0 on the first axis, everything on the second

	print 'maximum inflammation for patient 0:', patient_0.max()
	
	print data.mean(axis=0)
	
Plotting stuff:

%matplotlib inline

from matplotlib import pyplot

pyplot.imshow(data)

pyplot.show()

avg_inflammation = data.mean(axis=0)

pyplot.plot(ave_inflammation)

pyplot.show()
	
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

*no arg / return: print zero

*arg / return: initials

> BMI etc. as exercise

Talk about default values, multiple returns

Talk about documenting code with comments

Segue into numpy - create "analyze" function

##Logic and Flow Control

###For Loops

Um...printing a list?  

length = 0
for vowel in 'aeiou':
    length = length + 1
print 'There are', length, 'vowels'

###If/Then Statements

~~~
x = 5
if x < 0:
    print "x is negative"
else:
    print "x in non-negative"
~~~

heatmap cumulative exercise

Let's start by creating some simple heat maps of our own using a library called ipythonblocks. The first step is to create our own "image":

	from ipythonblocks import ImageGrid, colors
	
	sample = ImageGrid(4,4)
	sample.show()
	sample[0,0] = colors['Red']

	import numpy as np

	data = np.loadtxt(fname='inflammation-01.csv', delimiter=',')

	print 'data shape:', data.shape

The second is to create an image grid that is the same size as the data:

	width, height = data.shape
	
	heatmap = ImageGrid(width, height)
	
	
	for x in range(width):
    for y in range(height):
        if data[x, y] < data.mean():
            heatmap[x, y] = colors['Red']
        elif data[x, y] == data.mean():
            heatmap[x, y] = colors['Green']
        else:
            heatmap[x, y] = colors['Blue']
	heatmap.show()

Alterations: orientation, block size, colors, mean calculation.  
	
	flipped = data.transpose()
	width, height = flipped.shape
	heatmap = ImageGrid(width, height, block_size=5)
	center = flipped.mean()
	for x in range(width):
    for y in range(height):
        if flipped[x, y] < (0.8 * center):
            heatmap[x, y] = colors['Orchid']
        elif flipped[x, y] > (1.2 * center):
            heatmap[x, y] = colors['HotPink']
        else:
            heatmap[x, y] = colors['Fuchsia']
	heatmap.show()

We could rewrite our loop a third time, but the right thing to do is to put our code in a function so that we can experiment with bands and colors more easily.

def make_heatmap(values, low_color, mid_color, high_color, low_band, high_band, block_size):
    '''Make a 3-colored heatmap from a 2D array of data.'''
    width, height = values.shape
    result = ImageGrid(width, height, block_size=block_size)
    center = values.mean()
    for x in range(width):
        for y in range(height):
            if values[x, y] < low_band * center:
                result[x, y] = low_color
            elif values[x, y] > high_band * center:
                result[x, y] = high_color
            else:
                result[x, y] = mid_color
    return result

To test this function, we'll run it with the settings we just used:

	h = make_heatmap(flipped, colors['Orchid'], colors['Fuchsia'], colors['HotPink'], 0.8, 1.2, 5)
	h.show()

That seems right, so let's widen the band and use more dramatic colors:

	h = make_heatmap(flipped, colors['Gray'], colors['YellowGreen'], colors['SpringGreen'], 0.5, 1.5, 5)
	h.show()
	
Add default values.  

##Scripting in the Shell

~~~
import sys

print 'version is', sys.version
print 'arguments are', sys.argv
~~~

import sys
import numpy as np

def main():
    script = sys.argv[0]
    action = sys.argv[1]
    filenames = sys.argv[2:]

    for f in filenames:
        data = np.loadtxt(f, delimiter=',')

        if action == '--min':
            values = data.min(axis=1)
        elif action == '--mean':
            values = data.mean(axis=1)
        elif action == '--max':
            values = data.max(axis=1)

        for m in values:
            print m

main()

OR

%matplotlib inline

import numpy as np
from matplotlib import pyplot as plt

def analyze(filename):
    data = np.loadtxt(fname=filename, delimiter=',')
    
    plt.figure(figsize=(10.0, 3.0))
    
    plt.subplot(1, 3, 1)
    plt.ylabel('average')
    plt.plot(data.mean(0))
    
    plt.subplot(1, 3, 2)
    plt.ylabel('max')
    plt.plot(data.max(0))
    
    plt.subplot(1, 3, 3)
    plt.ylabel('min')
    plt.plot(data.min(0))
    
    plt.tight_layout()
    plt.show()

analyze('inflammation-01.csv')
