#Shell Script

Tabs to have open: etherpad and terminal. 

##Intro + motivation (10 min)

A shell is just a different way of doing many of the things you would accomplish w/ clicking or using keyboard shortcuts on a visual interface.  

BUT, it's not like you've opened up a direct line to your computer's motherboard here, the shell is just another interpreter between you and the motherboard, in the same way that your typical graphical interface is.  Just now you're primarily typing instead of clicking.  

Semantics: this most generally is called a command line interface, but people more commonly refer to bash, or shell, or a bash shell, to talk about the specific sort of command line interface they're using.  

So, what can you DO with this command line interface?  Well, lots of things.  This is not going to be an exhaustive summary of shell commands, although we will end up using a lot of them.  But I want to present this guiding question which we'll come back to throughout the lesson (hopefully).  

> Slide: What would be easier to accomplish using the shell?  What would be harder?  If this was your primary interface tool, would your workflow/process be different?  How so?  

##Files + directories (30 min)

> Objective : use shell commands to explore a filesystem

> Objective : navigate between directories in multiple ways

> Objective : compare and contrast navigating the file system w/ a command line vs. a gui

The first thing to say, when you're in a command line interface, is that location matters.  We'll be spending a fair bit of time on this, because it's both one of the most important practical and conceptual skills associated w/ using the command line.  It's also pretty basic, so this will be a bit slow to the command line veterans - just stick with me!  

Directories as nested locations.  In a visual interface, we're used to a sort of "top down" vision of our directories.  If you think of the directories (folders) on your computer as nested boxes, we're always sort of reaching in from outside to look at them.  But from the command line, we're inside the box and we can only see what's inside the box with us.  So always important is knowing where you are.  That command is three letters: pwd.  

`$pwd`

This shouldn't be too hard to decipher - based on this return, which is called a "path".  This path tells me a couple of things: where I am now, and which other directories I'm included in.  

Now who is this person who is in this directory?  Who am I? Well...

`$whoami`

will tell me.  

Now we want to see what else is in our directory with us.  The command for that is: 

`$ls`

And finally, we want to move to a different directory.  That command is `cd` for "change directory."  

~~~
$cd Desktop
~~~

And now we can look at the files in this direction. `ls`

What else to do you need to know to traverse your entire file structure?  

Need to go up as well as down!  Ask veteran for path: 

`$cd ..`

The `cd` command on its own will take you back to the home directory.  If you 
get lost, just go back there.  Also, `ls` can have arguments.  And tab completion.  

Now, supposed I actually want to get to the shell lesson materials.  

> put directions up!!

> make a directory, download zip, move there + unzip

> find unzipped directory - look at contents, get to /nelle

> try to draw a quick sketch of her directory

* briefly touch on relative vs absolute paths
* `cd` into creatures, demo `ls` w/ molecules
* example: `ls /Users/` w/o moving

Let's talk about options first. 

~~~
$ ls -l 
$ ls -l -a
$ ls -la
$ ls -lah
~~~

> Do Challenges

> Some sort of question about link between filesystems + interface -> write answers on board

Summarize our tools: `pwd`, `ls`, and `cd`

## Creating Things (aim for 20 min or less)

*   Create a directory hierarchy that matches a given diagram.
*   Create files in that hierarchy using an editor or by copying and renaming existing files.
*   Display the contents of a directory using the command line.
*   Delete specified files and/or directories.


We now know how to explore files and directories, but how do we create them in the first place? Let's go back to Nelle's home directory.  

Let's create a new directory called `thesis`

> Open folder to show this!  

~~~
$ mkdir thesis
~~~

As you might (or might not) guess from its name,
`mkdir` means "make directory".
Since `thesis` is a relative path
(i.e., doesn't have a leading slash),
the new directory is made below the current working directory:

~~~
$ ls
~~~

However, there's nothing in it yet:

~~~
$ ls thesis
~~~

Let's change our working directory to `thesis` using `cd`,
then run a text editor called Nano to create a file called `draft.txt`:

~~~
$ cd thesis
$ nano draft.txt
~~~

Let's type in a few lines of text,
then use Control-O to write our data to disk:

Once our file is saved,
we can use Control-X to quit the editor and return to the shell.
(Unix documentation often uses the shorthand `^A` to mean "control-A".)
`nano` doesn't leave any output on the screen after it exits,
but `ls` now shows that we have created a file called `draft.txt`:

~~~
$ ls
~~~

Let's move `quotes.txt` into nelle/

~~~
$ mv draft.txt ..
~~~

> How would that command have been different if I had been in nelle/ ?

The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `thesis` is empty:

`draft.txt` isn't a particularly informative name,
so let's change the file's name using `mv`,
which is short for "move":

~~~
$ mv draft.txt quotes.txt
~~~

Further,
`ls` with a filename or directory name as a parameter only lists that file or directory.
We can use this to see that `quotes.txt` is still in our current directory:

The `cp` command works very much like `mv`,
except it copies a file instead of moving it.

~~~
$ cp quotes.txt thesis/quotes.txt
~~~

Removing things is as simple as

~~~
rm quotes.txt
~~~

DELETING IS FOREVER.  Once you delete something using rm it will not return unless you are using version control - which is what we'll be talking about after lunch.

~~~
rmdir thesis
~~~

Two ways: delete file 

Also, `rm -r` to delete the Desktop directory

The beautiful thing about options is that there is usually some consistency - something like -f is usually force, -r is recursive, -a is all and so on, -h is human readable and -v is verbose.

+ then remove OR rm -r

Fancy copying: in molecules:

~~~
mkdir originals
cp *.pdb originals/
~~~

> again ask: what is different about making/moving/copying files in this way?  


##Command line commands (at least 15 min)

> Objective: Research previously unknown commands

> Objective: Explain the "format" of a typical command line command

All these commands we've been typing - they're actually a bunch of mini-programs.  Your command line has a special variable where it looks for programs - if it's in the PATH it can be run from the command line.  

`echo $PATH`

There are a BUNCH more commands we can run, plus, options.  

How to find out about these commands: `$man` or google.  

> Give example of a bunch of commands, talk out the syntax

> Copy commands to etherpad, have people take notes

* echo
* less
* cat
* head
* (tail)
* grep
* wc
* sort
* uniq
* find

> Assignment: find out about this command, tell us what this would do, other options, why it might be useful.  

> quiz: based on what we just talked about, what would you guess this command is?  (use cut)

[link](https://github.com/ChristinaLK/algorithms-seminar/tree/master/asst01)

#BREAK

##Intro to "part 2"

Before the break, we did a lot of pieces - individual programs.  Now we're going to start putting those little programs together in new ways.  This is the idea behind good software development, and it will come up when we talk about python as well: you're almost always better off building little code units that you can then string together into powerful sequences.  

##Pipes and Filters (25 min)

> Objective: identify the input/output chain for a piped process

First up is redirection.  The first part is easy - anything that prints to standard output can be redirected using a > symbol.  Like so: 

~~~
echo "Hello world!"
echo "hello world" > greeting.txt
ls
less greeting.txt
~~~

What happens if you redirect a different phrase to the same document?  To concatenate, do this: 

~~~
echo "- Call mom" >> notes.txt
~~~

> save your history and put it in the novice/shell/ folder

We're going to start in the molecules directory, which may now be in nelle/data, if your moves from the first half of the class worked.  If not, just find it wherever it is.  Remember: pwd, ls and cd and you can get where you need to go.  

~~~
cd data/molecules
~~~

Let's poke around and see what we have.  

~~~
ls
less cubane.pdb
~~~

Having done that, let's start actually calculating something from those files:

~~~
wc -l cubane.pdb
wc -l *.pdb
~~~

This is an easy list to eyeball and find the largest and smallest items.  But what if there were a LOT more?  (Run the previous command again.)  We want to take this output and somehow sort it.  There are TWO ways to do that.  

First, redirect to file.  We can save our output from the screen into a file, like so: 

~~~
wc -l *.pdb > lines
~~~

And then run sort on that.  

~~~
sort -n lines
~~~

But unless those intermediate steps matter, you don't really want to be cluttering up your directory with intermediate files.  So there's another way to achieve this kind of progression, the pipe.  

(do a board diagram)

~~~
wc -l *.pdb | sort -n
~~~

Now if I want to extract the shortest file, what should I add to my pipeline?  

~~~
wc -l *.pdb | sort -n | head -1
~~~

> Using what you know so far, write a pipe command that takes our sorted list and returns the LONGEST line length.  

Talk about that solution, run on pdb directory, to demonstrate.  

> Bunch o' exercises?  

> Ask question: how would this be useful to you in your research?  

##For loops

In this example,
we'll use the `creatures` directory which only has two example files,
but the principles can be applied to many many more files at once.
We would like to modify these files, but also save a version of the original files and rename them 
as `original-basilisk.dat` and `original-unicorn.dat`.
We can't use:

~~~ {.bash}
$ mv *.dat original-*.dat
~~~

because that would expand to:

~~~ {.bash}
$ mv basilisk.dat unicorn.dat original-*.dat
~~~

This wouldn't back up our files, instead we get an error

~~~ {.error}
mv: target `original-*.dat' is not a directory
~~~

This a problem arises when `mv` receives more than two inputs. When this happens, it
expects the last input to be a directory where it can move all the files it was passed.
Since there is no directory named `original-*.dat` in the `creatures` directory we get an
error.

Instead, we can use a **loop**
to do some operation once for each thing in a list.
Here's a simple example that displays the first three lines of each file in turn:

~~~ {.bash}
$ for filename in basilisk.dat unicorn.dat
> do
>    head -3 $filename
> done
~~~
~~~ {.output}
COMMON NAME: basilisk
CLASSIFICATION: basiliscus vulgaris
UPDATED: 1745-05-02
COMMON NAME: unicorn
CLASSIFICATION: equus monoceros
UPDATED: 1738-11-24
~~~

When the shell sees the keyword `for`,
it knows it is supposed to repeat a command (or group of commands) once for each thing in a list.
In this case, the list is the two filenames.
Each time through the loop,
the name of the thing currently being operated on is assigned to
the **variable** called `filename`.
Inside the loop,
we get the variable's value by putting `$` in front of it:
`$filename` is `basilisk.dat` the first time through the loop,
`unicorn.dat` the second,
and so on.

By using the dollar sign we are telling the shell interpreter to treat
`filename` as a variable name and substitute its value on its place,
but not as some text or external command. When using variables it is also 
possible to put the names into curly braces to clearly delimit the variable
name: `$filename` is equivalent to `${filename}`, but is different from
`${file}name`. You may find this notation in other people's programs.

Finally,
the command that's actually being run is our old friend `head`,
so this loop prints out the first three lines of each data file in turn.


We have called the variable in this loop `filename`
in order to make its purpose clearer to human readers.
The shell itself doesn't care what the variable is called;
if we wrote this loop as:

~~~ {.bash}
for x in basilisk.dat unicorn.dat
do
    head -3 $x
done
~~~

or:

~~~ {.bash}
for temperature in basilisk.dat unicorn.dat
do
    head -3 $temperature
done
~~~

it would work exactly the same way.
*Don't do this.*
Programs are only useful if people can understand them,
so meaningless names (like `x`) or misleading names (like `temperature`)
increase the odds that the program won't do what its readers think it does.

Here's a slightly more complicated loop:

~~~ {.bash}
for filename in *.dat
do
    echo $filename
    head -100 $filename | tail -20
done
~~~

The shell starts by expanding `*.dat` to create the list of files it will process.
The **loop body**
then executes two commands for each of those files.
The first, `echo`, just prints its command-line parameters to standard output.
For example:

~~~ {.bash}
$ echo hello there
~~~

prints:

~~~ {.output}
hello there
~~~

In this case,
since the shell expands `$filename` to be the name of a file,
`echo $filename` just prints the name of the file.
Note that we can't write this as:

~~~ {.bash}
for filename in *.dat
do
    $filename
    head -100 $filename | tail -20
done
~~~

because then the first time through the loop,
when `$filename` expanded to `basilisk.dat`, the shell would try to run `basilisk.dat` as a program.
Finally,
the `head` and `tail` combination selects lines 81-100 from whatever file is being processed.

Going back to our original file renaming problem,
we can solve it using this loop:

~~~ {.bash}
for filename in *.dat
do
    mv $filename original-$filename
done
~~~

This loop runs the `mv` command once for each filename.
The first time,
when `$filename` expands to `basilisk.dat`,
the shell executes:

~~~ {.bash}
mv basilisk.dat original-basilisk.dat
~~~

The second time, the command is:

~~~ {.bash}
mv unicorn.dat original-unicorn.dat
~~~

> `echo` trick

## Nelle's Pipeline: Processing Files

Nelle is now ready to process her data files.
Since she's still learning how to use the shell,
she decides to build up the required commands in stages.
Her first step is to make sure that she can select the right files --- remember,
these are ones whose names end in 'A' or 'B', rather than 'Z'. Starting from her home directory, Nelle types:

~~~ {.bash}
$ cd north-pacific-gyre/2012-07-03
$ for datafile in *[AB].txt
> do
>     echo $datafile
> done
~~~
~~~ {.output}
NENE01729A.txt
NENE01729B.txt
NENE01736A.txt
...
NENE02043A.txt
NENE02043B.txt
~~~

Her next step is to decide
what to call the files that the `goostats` analysis program will create.
Prefixing each input file's name with "stats" seems simple,
so she modifies her loop to do that:

~~~ {.bash}
$ for datafile in *[AB].txt
> do
>     echo $datafile stats-$datafile
> done
~~~
~~~ {.output}
NENE01729A.txt stats-NENE01729A.txt
NENE01729B.txt stats-NENE01729B.txt
NENE01736A.txt stats-NENE01736A.txt
...
NENE02043A.txt stats-NENE02043A.txt
NENE02043B.txt stats-NENE02043B.txt
~~~

She hasn't actually run `goostats` yet,
but now she's sure she can select the right files and generate the right output filenames.

Typing in commands over and over again is becoming tedious,
though,
and Nelle is worried about making mistakes,
so instead of re-entering her loop,
she presses the up arrow.
In response,
the shell redisplays the whole loop on one line
(using semi-colons to separate the pieces):

~~~ {.bash}
$ for datafile in *[AB].txt; do echo $datafile stats-$datafile; done
~~~

Using the left arrow key,
Nelle backs up and changes the command `echo` to `goostats`:

~~~ {.bash}
$ for datafile in *[AB].txt; do bash goostats $datafile stats-$datafile; done
~~~

When she presses enter,
the shell runs the modified command.
However, nothing appears to happen --- there is no output.
After a moment, Nelle realizes that since her script doesn't print anything to the screen any longer,
she has no idea whether it is running, much less how quickly.
She kills the job by typing Control-C,
uses up-arrow to repeat the command,
and edits it to read:

~~~ {.bash}
$ for datafile in *[AB].txt; do echo $datafile; bash goostats $datafile stats-$datafile; done
~~~

> ## Beginning and End {.callout}
>
> We can move to the beginning of a line in the shell by typing `^A`
> (which means Control-A)
> and to the end using `^E`.

When she runs her program now,
it produces one line of output every five seconds or so:

~~~ {.output}
NENE01729A.txt
NENE01729B.txt
NENE01736A.txt
...
~~~

1518 times 5 seconds,
divided by 60,
tells her that her script will take about two hours to run.
As a final check,
she opens another terminal window,
goes into `north-pacific-gyre/2012-07-03`,
and uses `cat stats-NENE01729B.txt`
to examine one of the output files.
It looks good,
so she decides to get some coffee and catch up on her reading.

##Scripts - Nelle

~~~
# Calculate reduced stats for data files at J = 100 c/bp.
for datafile in "$@"
do
    echo $datafile
    bash goostats -J 100 -r $datafile stats-$datafile
done
~~~

(The parameters `-J 100` and `-r` are the ones her supervisor said she should have used.)
She saves this in a file called `do-stats.sh`
so that she can now re-do the first stage of her analysis by typing:

~~~ {.bash}
$ bash do-stats.sh *[AB].txt
~~~

She can also do this:

~~~ {.bash}
$ bash do-stats.sh *[AB].txt | wc -l
~~~

so that the output is just the number of files processed
rather than the names of the files that were processed.

One thing to note about Nelle's script is that
it lets the person running it decide what files to process.
She could have written it as:

~~~
# Calculate reduced stats for  A and Site B data files at J = 100 c/bp.
for datafile in *[AB].txt
do
    echo $datafile
    bash goostats -J 100 -r $datafile stats-$datafile
done
~~~

The advantage is that this always selects the right files:
she doesn't have to remember to exclude the 'Z' files.
The disadvantage is that it *always* selects just those files --- she can't run it on all files
(including the 'Z' files),
or on the 'G' or 'H' files her colleagues in Antarctica are producing,
without editing the script.
If she wanted to be more adventurous,
she could modify her script to check for command-line parameters,
and use `*[AB].txt` if none were provided.
Of course, this introduces another tradeoff between flexibility and complexity.


##Scripts (25 min)

> Describe three reasons why you might save code in a script.

We can now "save our work" by putting everything we've done so far into a "script" - actually a program, but I'll probably mostly use the word script.  In our molecules directory, we'll make a document: 

~~~
nano sorting_script.sh
~~~

Use commands from previous exercise.  Can add shebang if you want, or run it using bash.  

~~~
bash sorting_script.sh
sorting_script.sh
~~~

> Have a discussion about scripts: why it is helpful to write them, etc. 

Now, this script is perfectly adequate, but it's not very flexible.  We can only use it in this directory.  It would be nice to be able to use it in several directories, in particular, both molecules and pdb.  So let's do some refactoring.  And while we're at it, we'll do some nice folder organization.  

~~~ 
cd ../
pwd
mkdir scripts
cp data/molecules/sorting_script.sh scripts/
~~~

Edit the script so that there's a path before the *.pdb.  Replace it with $1.  Save and close.  Diagram what's going to happen in terms of relative path.  

~~~
bash sorting_script.sh ../data/molecules
~~~

What if we wanted to be able to do this for not just pdb files?  What if we had a directory of text files?  Change the argument again.  Again, discuss location in the filesystem.  Maybe talk about $@?  

> Ask: what is missing?  

need comments!  Future you is never going to remember what this script does or what its arguments are.  Guaranteed.  Nobody has that much brain space.  

> Final discussion: any other advantages to command line tools?  

##Feedback (10 min)

(hopefully)
