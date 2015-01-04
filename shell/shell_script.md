#Shell Script

##Git Download
~~~
$git clone https://github.com/ChristinaLK/2015-01-05-wise-cuboulder
~~~

Tabs to have open: etherpad, exercise link, lesson (if you want)
and terminal, obviously.  

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
$cd 2015-01-05-wise-cuboulder
~~~

And now we can look at the files in this direction. `ls`

What else to do you need to know to traverse your entire file structure?  

Need to go up as well as down!  Ask veteran for path: 

`$cd ..`

Now, supposed I actually want to get to the shell lesson materials.  

`$cd 2015-01-05-wise-cuboulder`
`ls`

etc.  This is pretty laborious - it's like clicking through a bunch of windows.  Plus, we have these insanely long names.  SO, what can we do?  Let's talk "shortcuts"

* `cd` w/o an argument sends you back to "home"
* `ls` with path names
* sandwiching path names
* tab completion
* briefly touch on relative vs absolute paths

> Three different ways to get from /2015/novice/shell/filesystem/data/backup to nelle's molecules directory

> Make a quick diagram of nelle's directory using the command line

> Some sort of question about link between filesystems + interface -> write answers on board

##Creating Things (aim for 20 min or less)

*   Create a directory hierarchy that matches a given diagram.
*   Create files in that hierarchy using an editor or by copying and renaming existing files.
*   Display the contents of a directory using the command line.
*   Delete specified files and/or directories.


We now know how to explore files and directories, but how do we create them in the first place? Let's go back to Nelle's home directory.  

Let's create a new directory called `thesis`

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

> clean up nelle's home directory: try to delete Desktop, move molecules, animals, solar.pdf, pizza.cfg to data, rename notes.txt to to_do.txt

Let's talk about options first. 

~~~
$ ls -l 
$ ls -l -a
$ ls -la
$ ls -lah
~~~

Also, `rm -r` to delete the Desktop directory

The beautiful thing about options is that there is usually some consistency - something like -f is usually force, -r is recursive, -a is all and so on, -h is human readable and -v is verbose.

+ then remove OR rm -r

Fancy copying: in molecules:

~~~
mkdir originals
cp *.pdb originals/
~~~

> again ask: what is different about making/moving/copying files in this way?  

--------------

> Break

-------------

##Command line commands (at least 15 min)

> Objective: Research previously unknown commands

> Objective: Explain the "format" of a typical command line command

All these commands we've been typing - they're actually a bunch of mini-programs.  Your command line has a special variable where it looks for programs - if it's in the PATH it can be run from the command line.  

`echo $PATH`

There are a BUNCH more commands we can run, plus, options.  

How to find out about these commands: `$man` or google.  

> Give example of a bunch of commands, talk out the syntax

> Copy commands to etherpad, have people take notes

* less
* cat
* head
* (tail)
* grep
* echo
* wc
* sort

> Assignment: find out about this command, tell us what this would do, other options, why it might be useful.  

> quiz: based on what we just talked about, what would you guess this command is?  (use cut)

[link](https://github.com/ChristinaLK/algorithms-seminar/tree/master/asst01)

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
echo "- Call mom" >> to_do.txt
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

What if we wanted to be able to do this for not just pdb files?  What if we had a directory of text files?  Change the argument again.  Again, discuss location in the filesystem.  Maybe talk about $*?  

> Ask: what is missing?  

need comments!  Future you is never going to remember what this script does or what its arguments are.  Guaranteed.  Nobody has that much brain space.  

> Final discussion: any other advantages to command line tools?  

##Feedback (10 min)

(hopefully)
