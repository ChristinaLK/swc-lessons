#Git lessons

##Prep

* upload project_file directory, exercises, and commands
* have open in tabs: this file, star_logs, git_slides
* have terminal open

##Pre-lesson exercise

> file on-screen

##Slides

##Configuration

These are steps that only need be performed once.  Configuration.  
Do this and forget about it.  If you ever need to do it again, you can google.  

~~~
$ git config --global user.name “Christina Koch”

$ git config --global user.email "koch.christinal@gmail.com"

$ git config --global color.ui "auto"

$ git config --global core.editor "nano"
~~~

This type of configuration only needs to be done once--ever, unless you delete and reinstall git.  

> Describe the course of the lesson - tracking local changes before the break, syncing 
with a remote repository before lunch.  Mention that commands are listed in git-commands.  

##Local

###Basic git cycle

Interactive exercise: explain rationale (participation, etc.) 
> describe setup: room is directory, students are files, camera is repository
> have students all write down the number of years in undergrad/grad/post-grad
> all stand, hold card
> take a picture
> sit down, have all write area of research on pink card
> stage back row, take picture
> have front rows flip pink card and write last school they attended
> stage front rows, take a picture
> redo back row
> stage, take a picture

Click through slides on screen - this is the basic cycle of version control: creating a repo, 
adding/committing files, modifying files, adding committing files, etc.  So now we’re going to do this 
with commands in the bash shell.  Make sure everyone is in `project_files`.  

~~~
$git init
~~~

This creates our repository (the “folder” on my computer OR my camera)

~~~
$ls -a
~~~

Look at current status:

~~~
$git status

$git add git-commands.md
~~~

This adds modified files (the “changeset”) to our staging area (standing up)

$git status

$git add -A

$git commit -m “initializing repository”

Finally, this takes a snapshot, committing an image of all the files in the staging area (me taking a picture).

$git status

The goostats script produces multiple numbers

	bash goostats nene1729a.txt

Have them modify the shell script so only first line of goostats output is sent to file (pipe to head)

	$git status

Notice that our file is listed there.  

	$git add stats-script.sh

	$git status

File has moved - it’s now in the staging area (standing up) and is ready to be committed (captured)

	$git commit -m “Limiting input”

	$git status

Everything is up-to-date!

> Assignment: send output from script to output.txt and commit changes

### Tracking what's going on

Commits have labels, just like my demo in the beginning.  
In the same way that my camera automatically assigns names to my photos, 
the computer assigns a specific commit tag to each commit.  Let’s look at them.  

$git log
That’s a bit wordy though.  For the short version, use: 

$git log --oneline

There’s the labels.  

The alternative is to use HEAD notation.  HEAD is always the most recent commit, 
HEAD~1, the one before that, HEAD~2 the one before that, etc.  

Use image example - flip through the images to compare how data changed.  
It’s easy to tell which data was added because I had you write it on pink cards.  
We can actually do this with a git command.  

Add filename to output sequence  `echo $datafile >> output.txt`

$git diff

$git diff HEAD

$git diff HEAD (filename)

Now let’s commit our changes

$git add stats-script.sh

$git commit -m “Adding output files”

Let’s compare the previous revision (HEAD~1) w/ the first revision.  
$git diff (commitval)  HEAD~1 (filename)
$git diff (commitval)  HEAD~1
$git diff HEAD~1 (commitval)  

###Ignoring Files

Run our script - produces an output file

$git status

Final small task - maybe there are some files you don’t want to be tracking or versioning.  
Common examples: auxiliary files, automatically generated, etc.  

We can tell git to ignore these files by creating, appropriately enough, a file called “.gitignore.”  

$notepad .gitignore

add text and save

$git status

$git add .gitignore

$git commit -m

run script on different file

$git status

We can see that the file is not being tracked.  If you change the .gitignore file to remove the filename, it will be tracked again.  

Word to the wise: hard to untrack a file once it’s been tracked.  Do this right away! 

> Take a quick 4 minute break, have them describe the processes we've discussed.  Then have them diagram.  

##Git Remote

Recap where we've been.  Now we're going to move online - like google documents or dropbox.  

###Creating + connecting remote repositories

Two ways to make a repository on the github site: forking or a new directory.  
The major difference is whether it starts as empty or not, and its link with its “parent” directory.  

Create repository on github WITH README.  Look at address.  

$git remote add (name) (address)

The convention is to use clear names, origin + upstream are common.  
There are also other ways to add addresses, but https is the easiest to master at first.  
If we want to see the remotes we’ve programmed, we can type in

$git remote

$git remote -v

###Syncing files

Great, now we’ve set up a remote but we need to get them to talk to each other.  
Like they have each other’s number but now they need to be able to call each other.  
We do this with push/pull commands.  To push your files to the “upstream” repository, just do: 

~~~
$git push upstream master
~~~

> Project thing

~~~
$git pull upstream master

$git status / git log --oneline
~~~

> Edit the README, commit, push upstream

###git clone

What if you want to work on someone else’s directory?  i.e. make a copy of 
my github page, make some edits, and then push changes back.  Which shell/git commands 
you have learned so far would be necessary to do the above task?  
(In groups, have people come up with a list of the commands, then read them out one by one)

$mkdir target

$cd target

$git init

$git remote add origin https://github.com/ChristinaLK/location

$git pull origin master

Someone was like: we do this all the time, we should make this into a single command.  
Hence $git clone.  
This is how we created the directory from the start of class.  

$cd (directoryname)

$git remote -v

$git status

$git log

> Pause for note-taking, review, questions.  

Have everyone clone their neighbors remote repository

$git clone (https:// ... )

Add some sort of file (add/commit)

###Conflicts

Instructions in "exercises" file.  Edit own, push.  Edit others, try to push.  Pull, hopefully conflict is generated.  

	nano paper.txt
	
See the weird symbols here?  That's git's way of telling you that it's confused.  Unfortunately there's no nicely automated way to do this...you have to go through manually and select which bits you want to keep and which you want to throw away.  

##Optional Material (Local)

### Restoring Files (checkout part one)

Change script, to multiple output files: `python goostats.py $datafile > stats-$datafile`, commit changes.

Run file.  (`bash stats-script.sh`) Not what we wanted.  One of the much-touted reasons for version control is that you can’t break things.  So let’s break some things and see what happens.  

$rm stats*

$ls

$git diff

(can use HEAD or filename, but don’t have to)

Our magic command is going to be called “checkout” - to change metaphors, 
if we think of the commits as editions of a book on a shelf, we’re checking out a previous version.  
Caution: not including filename does different things, so you really want to think of this as reverting one file at a time. 

$git checkout HEAD stats-script.sh

Look at your file.  Is it back to the way it was before?  
Let’s see what’s happening:

$git status

What if we want to go back to an earlier file, either for reference or because we like it better or we broke something, 
but we already committed our changes?  Same process!

$git log --oneline
$git checkout (commithash) (filename)
$git status

If we want to keep this file the way it is (or was) we need to make a new commit.  So:

$git commit -m "restoring script file"

Make sure you checkout the file BEFORE the problem commit, if you’re fixing something.  

What happens if we checkout an old commmit?  

### Branching (checkout part 2) 

We want to go back and retool our output script again, but we don't want to lose our current version of the script.  

$git checkout (commithash)

$git branch new-output

$git checkout new-output

Edit script: add mkdir $1 and >> $1/stats-$filename

Draw a diagram on the board.  We can make changes in one branch independently of the other.  

$git checkout master

### Merging

Want to merge branches.  

$git merge new-output

Fix up stats script

$git add stats-script.sh

$git commit -m "merging in new output files"

(pcottle app)

> Talk about workflows (commit early, commit often or branch, edit, commit, merge)

##Optional Material (Remote)

###Collaborating via pull request

Try pushing to the repo - can’t, don’t have permissions.  Talk about why.  
If I want all of you to contribute - but I want to control your contribution, enter pull requests.  

Fork lessons repository - explain what is happening here.  (difference between fork + branch)
Add this fork as upstream to current repository

$git remote add upstream (address)

$git push upstream master

In your last pull from origin, should have gotten a folder named participants.  Inside, there’s a bio text file.  Edit the file, stage, commit.  Push to your fork.  (directions in etherpad?)

$notepad bio.txt

$git add christina.txt

$git commit -m “adding Christina’s bio”

$git push upstream master

Now submit pull request.  

###Workflows

Now that we have this tool, we need some best practice of how to use it.  This is the hardest part of learning a new tool, because it’s developing new habits, which is tricky.  
Strategies: put up reminder notes? etc. etc. Use diagram on board to illustrate cycle.  
Local
create repository: $git init or $git clone
basic cycle: add/commit, add/commit, use checkout as necessary
development: branch (checkout), add/commit, merge when development is done
Collaborative

(have second bash window open)
Demonstrate my process in contributing to the bootcamp repo - make sure my changes aren’t the last ones
$git push origin gh-pages
$git pull origin gh-pages
$git push origin gh-pages

create repositories: $git clone, or fork/create new and $git remote add
basic cycle: pull, edit/add/commit, pull again, merge if necessary, push
pull, branch, edit/add/commit, push to fork, submit pull request, pull final result

Have list of scenarios - what should you do?  

Review
what are the two ways to create a repo online? (directly or via a fork)
what are the two ways to create a repo locally? (git init or cloning)
what are the two ways to link a local/remote? (use remote add or clone)
have worksheet?  

## Resources
*branching app: http://pcottle.github.io/learnGitBranching/?NODEMO
*atlassian: https://www.atlassian.com/git/tutorial/git-basics
*git site: http://git-scm.com/
*GUI interfaces:  http://git-scm.com/downloads/guis
*SWC site: http://software-carpentry.org/
*diff visualizers, like https://sourcegear.com/diffmerge/
* starlogs.net
