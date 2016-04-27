# "Capstone" Material

This exercise can be done after the initial SWC lessons on python, shell and git.  
It assumes that writing python scripts (outside the notebook) was not covered 
in the teaching of the python section.  

## Informal Script + Commands

The goal of this session is to pull together some of the pieces we've discussed, 
to see what they would look like as part of a real project.  

Have a plaintext editor open, and 
start in the same python-novice-inflammation data folder as yesterday.  

~~~
$ cd ~/Desktop/python-novice-inflammation/data
$ ls
~~~

Explain different ways to run python: 
* in notebook
* in python console (demo briefly)
* as script

Create script file called `readings.py` in text editor, and have "hello world" example
as initial code:
~~~
print("hello world")
~~~
~~~
$ python readings.py
~~~

Sidebar: would normally comment out that "hello world" line or delete it.  Another 
way to save is make the directory a repository.  Do that + commit file.  
~~~
$ git init
$ git add readings.py
$ git commit -m "hello world statement"
~~~

Now make changes.  
We're going to do more than print - we're going to do analysis.  Recap of yesterday: 
~~~
import numpy
data = numpy.loadtxt('inflammation-01.csv', delimiter=',')
value = data.mean(axis = 1)
print(value)
~~~

Works - commit it.  
~~~
$ git add readings.py
$ git commit -m "finding the mean of one file"
~~~

Next, explain command line syntax.  Want to be able to pass filename into 
file instead of hard coding, like so: 
~~~
$ python readings.py inflammation-01.csv
~~~

To do that, need library: 

~~~
import sys
import numpy

print('version',sys.version)
print('sys.argv',sys.argv)

data = numpy.loadtxt('inflammation-01.csv', delimiter=',')
value = data.mean(axis = 1)
print(value)
~~~

Test it out.  WHat happens with no filename?  WIth one filename?  WIth random args?
~~~
$ python readings.py
$ python readings.py inflammation-01.csv
$ python readings.py inflammation-01.csv apples cherries
~~~

What *is* sys.argv?  (a list of strings)

Commit changes.  
~~~
$ git add readings.py
$ git commit -m "using sys library"
~~~

Which element of the list is the filename?  (index: 1)
add filename variable to script.  I usually save the script name as well, 
since that keeps me honest about where things are in the sys.argv list.  

~~~
import sys
import numpy

script = sys.argv[0]
filename = sys.argv[1]

data = numpy.loadtxt('inflammation-01.csv', delimiter=',')
value = data.mean(axis = 1)
print(value)
~~~

Try running it - it should work, commit changes.  
~~~
$ python readings.py inflammation-01.csv
$ git add readings.py
$ git commit -m "using sys library"
~~~

Now clean up script, putting stuff into a function: 
~~~
import sys
import numpy

script = sys.argv[0]
filename = sys.argv[1]

def reading(filename):
	data = numpy.loadtxt(filename, delimiter=',')
	value = data.mean(axis = 1)
	print(value)

reading(filename)
~~~

Check if it works, commit.  
~~~
$ python readings.py inflammation-01.csv
$ git add readings.py
$ git commit -m "moved analysis into function"
~~~

Add options - want to enter this on command line: 
~~~
$ python readings.py --mean inflammation-01.csv
~~~

What needs to be changed?  First, in sys.argv, then, adding conditional statement 
to function.  
~~~
import sys
import numpy

script = sys.argv[0]
option = sys.argv[1]
filename = sys.argv[2]

def reading(filename):
	data = numpy.loadtxt(filename, delimiter=',')
	if option == 'mean':
		value = data.mean(axis = 1)
	print(value)

reading(filename)
~~~

Check if it works, commit: 
~~~
$ python readings.py --mean inflammation-01.csv
$ git add readings.py
$ git commit -m "added mean option"
~~~

Students can do the following exercise.  Green stickies go up once they've done 
at least *one* additional option; fast people can do 2-3.  

> ### Scripting

> Implement another statistical measure (standard deviation, maximum or minimum)
> in our script.  Commit your changes once you've checked it worked!  

Compare / contrast using plain ifs to elifs.  I also suggested including 
an "else" clause with an error message at the end - but also pointed out that 
if you *want* the script to error out if you use an improper option, that's 
not what you should do.  Someone made the (wise) suggestion, that my error 
message could include which options *were* supported!  

~~~
import sys
import numpy

script = sys.argv[0]
option = sys.argv[1]
filename = sys.argv[2]

def reading(filename):
	data = numpy.loadtxt(filename, delimiter=',')
	if option == 'mean':
		value = data.mean(axis = 1)
	elif option == 'std':
		value = data.std(axis = 1)
	else: 
		value = "option not supported"
	print(value)

reading(filename)
~~~

~~~
$ git add readings.py
$ git commit -m "added std deviation option and error message"
~~~

Finally, loops.  Can do a bash loop and/or a loop inside the script.  Bash loop 
felt more authentic, but you miss out on the Python syntax, so I did both.  

~~~
for file in inflammation*.csv
do
python readings.py --mean $file
done
~~~

vs

~~~
import sys
import numpy

script = sys.argv[0]
option = sys.argv[1]
filenames = sys.argv[2:]

def reading(filename):
	data = numpy.loadtxt(filename, delimiter=',')
	if option == 'mean':
		value = data.mean(axis = 1)
	elif option == 'std':
		value = data.std(axis = 1)
	else: 
		value = "option not supported"
	print(value)

for file in filenames:
	reading(file)
~~~

Commit changes (if any): 
~~~
$ git add readings.py
$ git commit -m "added loop"
~~~

Exercise: I had students do the following (before optional), and then, when I brought 
everyone back together, went around the room calling on people, having them tell me 
which command I should run next.  I didn't do the optional stages, but talked about 
what they mean and why you'd do them.  

> ### Organization
> 
> * Implicit first step: check where you are.  
> * Create a `code` subdirectory.  
> * Move script and notebook to `code` directory.  
> * Rename your notebook to something more descriptive.  
> * Create a `data` subdirectory
> * Move data files to `data`.  
> * Commit changes
> * Create a README file.  
> * Commit changes.  
> 
> Optional:
> * Create a LICENSE file.  (See [this page](http://swcarpentry.github.io/git-novice/11-licensing.html))
> * Create a data README.  
> * Create a "master" script in the main level directory.  
> * Put your directory/repository on GitHub.  


## Notes

* I waited to motivate a git repo until we were making changes to a file.  
Could also do it at the very beginning, before even starting the lesson.  
* Where you create the repo + how people organize the directories depends a little 
on how diligent everyone was in creating `python-novice-inflammation` on their 
desktop and then putting the `data` dir inside.  I just did everything inside of 
`data` b/c some participants hadn't create the parent dir.  In a perfect world, 
everyone has a parent dir, which is where the repo should go, and you don't 
need to move the data files around when you organize - the scripts move up and then 
into a `scripts` directory in `python-novice-inflammation`.  
* Building on point one, reorganization could happen *before* scripting.  I went for 
the "realism" of organizing after the fact.  :P  
* I realize that I'm not following the "best" script conventions here - I don't have 
a "main" function, for example.  This, to me, seemed slightly less complicated but 
at least gets the idea of functions across.  
* Also not using great style for dealing with args - worth mentioning that in a real 
script with lots of options, would use a library for that instead of crude cond. statement. 
* Another potential exercise would be for them to add *another* option that allows 
you to choose which axis you're running on.  
* I was inconsistent - I used `filename` as an argument to the function, but not 
the `option`, even tho both change.  
* Genuine typos included forgetting a colon after my function defintion.  Demonstrative 
errors included running script w/o input file and getting index error.  
* This took ~ 1 hr and 20 min.  
* I had people use plaintext editors of choice and that didn't seem to throw anyone 
for a loop, really.  
* Screen real estate is hard - I had to have everything big enough to be seen, which 
meant that I couldn't have each window (shell/editor) on half the screen, which 
would have been better.  You don't need much shell real estate, since you're just 
running the same command over and over.  