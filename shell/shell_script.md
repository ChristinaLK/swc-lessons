#Shell Script

##Git Download
~~~
$git clone https://github.com/ChristinaLK/2015-01-05-wise-cuboulder
~~~

##Intro + motivation

A shell is just a different way of doing many of the things you would accomplish w/ clicking or using keyboard shortcuts on a visual interface.  

BUT, it's not like you've opened up a direct line to your computer's motherboard here, the shell is just another interpreter between you and the motherboard, in the same way that your typical graphical interface is.  Just now you're primarily typing instead of clicking.  

Semantics: this most generally is called a command line interface, but people more commonly refer to bash, or shell, or a bash shell, to talk about the specific sort of command line interface they're using.  

So, what can you DO with this command line interface?  Well, lots of things.  This is not going to be an exhaustive summary of shell commands, although we will end up using a lot of them.  But I want to present this guiding question which we'll come back to throughout the lesson (hopefully).  

> Slide: What would be easier to accomplish using the shell?  What would be harder?  If this was your primary interface tool, would your workflow/process be different?  How so?  

##Files + directories

> Objective : use shell commands to explore a filesystem
> Objective : navigate between directories in multiple ways
> Objective : compare and contrast navigating the file system w/ a command line vs. a gui

The first thing to say, when you're in a command line interface, is that location matters.  We'll be spending a fair bit of time on this, because it's both one of the most important practical and conceptual skills associated w/ using the command line.  It's also pretty basic, so this will be a bit slow to the command line veterans - just stick with me!  

Directories as nested locations.  In a visual interface, we're used to a sort of "top down" vision of our directories.  If you think of the directories (folders) on your computer as nested boxes, we're always sort of reaching in from outside to look at them.  But from the command line, we're *inside* the box and we can only see what's inside the box with us.  So always important is knowing where you are.  That command is three letters: pwd.  

`$pwd`

This shouldn't be too hard to decipher - based on this return, which is called a "path".  This path tells me a couple of things: where I am now, and which other directories I'm included in.  

Now who is this person who is in this directory?  Who am I? Well...

`$whoami`

will tell me.  

Now we want to see what else is in our directory with us.  The command for that is: 

`$ls`

And finally, we want to move to a different directory.  That command is `cd` for "change directory."  

~~~
$cd 2015-01-05-wise-cuboulder
~~~

And now we can look at the files in this direction. `ls`

What else to do you need to know to traverse your entire file structure?  

Need to go up as well as down!  Ask veteran for path: 

`$cd ..`

Now, supposed I actually want to get to the shell lesson materials.  

`$cd 2015-01-05-wise-cuboulder`
`ls`

etc.  This is pretty laborious - it's like clicking through a bunch of windows - ugh.  Plus, we have these insanely long names.  SO, what can we do?  Let's talk "shortcuts"

* `cd` w/o an argument sends you back to "home"
* sandwiching path names
* tab completion
* briefly touch on relative vs absolute paths

Explore filesystem

> Choose your own (filesystem) adventure! / Different ways to jump between files
> Some sort of question about link between filesystems + interface -> write answers on board

##Creating Things (aim for 15 min or less)

> basically use Creating things verbatim

#### Objectives
*   Create a directory hierarchy that matches a given diagram.
*   Create files in that hierarchy using an editor or by copying and renaming existing files.
*   Display the contents of a directory using the command line.
*   Delete specified files and/or directories.


We now know how to explore files and directories,
but how do we create them in the first place?
Let's go back to Nelle's home directory,
`/users/nelle`,

Let's create a new directory called `thesis` using the command `mkdir thesis`
(which has no output):

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

`draft.txt` isn't a particularly informative name,
so let's change the file's name using `mv`,
which is short for "move":

~~~
$ mv draft.txt quotes.txt
~~~

Sure enough,
`ls` shows us that `thesis` now contains one file called `quotes.txt`:

~~~
$ ls thesis
~~~
{:class="in"}
~~~
quotes.txt
~~~
{:class="out"}

Just for the sake of inconsistency,
`mv` also works on directories&mdash;there is no separate `mvdir` command.

Let's move `quotes.txt` into nelle/
We use `mv` once again,
but this time we'll just use the name of a directory as the second parameter
to tell `mv` that we want to keep the filename,
but put the file somewhere new.
(This is why the command is called "move".)
In this case,
the directory name we use is the special directory name `.` that we mentioned earlier.

~~~
$ mv quotes.txt ..
~~~

> How would that command have been different if I had been in nelle/ ?

The effect is to move the file from the directory it was in to the current working directory.
`ls` now shows us that `thesis` is empty:

~~~
$ ls thesis
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

DELETING IS FOREVER.  

~~~
rmdir thesis
~~~

Two ways: delete file + then remove OR rm -r

> clean up nelle's home directory

##Command line commands

> Explain the "format" of a typical command line command

All these commands we've been typing - they're actually a bunch of mini-programs.  Your command line has a special variable where it looks for programs - if it's in the PATH it can be run from the command line.  

`echo $PATH`

There are a BUNCH more commands we can run.  

less
cat
wc
grep
echo

one drawback / one useful thing

talk about flags and arguments and more path stuff

The beautiful thing about options is that there is actually some consistency - something like -f is usually force, -r is recursive, -a is all and so on, -h is human readable and -v is verbose.

> slide: what would you guess this command is?  
> slide2: more command guesses

What's the difference between an argument and an option?  

--------------



##Pipes and Filters (20-30 min)
