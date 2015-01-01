#Shell Script

##Git Download
$git clone (link) (master)

##Intro + motivation

A shell is just a different way of doing many of the things you would accomplish w/ clicking or using keyboard shortcuts on a visual interface.  

BUT, it's not like you've opened up a direct line to your computer's motherboard here, the shell is just another interpreter between you and the motherboard, in the same way that your typical graphical interface is.  Just now you're primarily typing instead of clicking.  

Semantics: this most generally is called a command line interface, but people more commonly refer to bash, or shell, or a bash shell, to talk about the specific sort of command line interface they're using.  

So, what can you DO with this command line interface?  Well, lots of things.  This is not going to be an exhaustive summary of shell commands, although we will end up using a lot of them.  But I want to present this guiding question which we'll come back to throughout the lesson (hopefully).  

> Slide: What would be easier to accomplish using the shell?  What would be harder?  If this was your primary interface tool, would your workflow/process be different?  How so?  

##Files + directories

> Objective : navigate 

The first thing to say, when you're in a command line interface, is that location matters.  In a visual interface, we're used to a sort of "top down" vision of our directories.  If you think of the directories (folders) on your computer as nested boxes, we're always sort of reaching in from outside to look at them.  But from the command line, we're *inside* the box and we can only see what's inside the box with us.  So always important is knowing where you are.  That command is three letters: pwd.  

$pwd

This shouldn't be too hard to decipher - based on this return, which is called a "path," 

Who is this person who is in this directory?  Who am I? Well...

$whoami

will tell me.  

Now we want to see what else is in our directory with us.  The command for that is: 

$ls

And finally, we want to move to a different box.  That command is `cd` for "change directory."  

~~~
$cd 2014-whatevers
~~~

And now we can look at the files in this direction.   

will always take you to your "home" location, and from there, you can cd into this directory.  What else to do you need to know to traverse your entire file structure?  
Need to go up as well as down!  That's simple: ..

$cd ..

Go through a bunch of directories:

This is pretty laborious - it's like clicking through a bunch of windows - ugh.  Plus, we have these insanely long names.  SO, what can we do?  Two things:

* path names

~~~
$cd ../../../..
$pwd
$cd ..
$ls
$cd 
~~~

* tab completion

Choose your own (filesystem) adventure!  

If you get hopelessly lost, you can always just type: 
$cd
and you'll go back to your home directory, and you can start again from there.  
(write exercise)
(and solution)

Some sort of question about link between filesystems + interface

##Command line commands

> Explain the "format" of a typical command line command

All these commands we've been typing - they're actually a bunch of mini-programs.  

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

##Creating Things (aim for 15 min or less)

$mkdir

$nano (or notepad)
Create text file

cp
mv
rm

##Pipes and Filters (20-30 min)