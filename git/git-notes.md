#Git lessons

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
with commands in the bash shell.  Make sure everyone is in moved folder.  

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

$git add -A
~~~

This adds modified files (the “changeset”) to our staging area (standing up)

$git status
$git commit -m “initializing repository”

Finally, this takes a snapshot, committing an image of all the files in the staging area (me taking a picture).

$git status

Have them create a shell script that finds rows w/ the work “Question,” top 10 rows

$notepad nearest_planets.sh

grep “Question” Analytics_Fall2013.csv | head

$git status

Notice that our file is listed there.  

$git add top_10.sh

$git status

File has moved - it’s now in the staging area (standing up) and is ready to be committed (captured)

$git commit -m “adding git notes”

$git status

Everything is up-to-date!

Assignment: 
> Not sure yet.  

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

Add output pipe to script.  Don’t commit, don’t do anything!  Just save.  
$git diff
$git diff HEAD
$git diff HEAD (filename)

Now let’s commit our changes
$git add (filename)
$git commit -m “Adding output files”

Let’s compare the previous revision (HEAD~1) w/ the first revision.  
$git diff (commitval)  HEAD~1 (filename)
$git diff (commitval)  HEAD~1
$git diff HEAD~1 (commitval)  

###Ignoring Files

Run our script - produces an output file.  

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

> Take a quick 4 minute break, have folks take notes in the git-commands document and commit their changes.  

### Restoring Files (checkout part one)

One of the much-touted reasons for version control is that you can’t break things.  So let’s break some things and see what happens.  
$rm top_10.sh
Let’s see the damage:
$git diff
(can use HEAD or filename, but don’t have to)

Our magic command is going to be called “checkout” - to change metaphors, 
if we think of the commits as editions of a book on a shelf, we’re checking out a previous version.  
Caution: not including filename does different things, so you really want to think of this as reverting one file at a time. 
 
$git checkout HEAD top_10.sh

Look at your file.  Is it back to the way it was before?  
Let’s see what’s happening:

$git status

What if we want to go back to an earlier file, either for reference or because we like it better or we broke something, 
but we already committed our changes?  Same process!

$git log --oneline
$git checkout (commithash) (filename)
$git status

If we want to keep this file the way it is (or was) we need to make a new commit.  So:

$git commit -m “returning old analytics file”

Make sure you checkout the file BEFORE the problem commit, if you’re fixing something.  

What happens if we checkout an old commmit?  

### Branching (checkout part 2) 

Do a MAJOR re-edit of your paper, but don't want to lose the previous copy.  

Use pcottle app?  

Do basic branches/merges, w/ simple file editing
Use paperweight analogy
Conclusion

Give everyone two minutes to take notes - put in notes file in other directory
Take questions on etherpad
Put links on etherpad
worksheet?

### Merging

The same merging problem can occur locally.  Make changes on one branch, then another, then merge branches.  

$git branch name

$git checkout name

make changes, add, commit

$git checkout master

make changes, add, commit

$git merge name

> Longer break (10:30 - 11:00), make sure everyone has github account

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

But that doesn't work!  What's going on?  Github thinks that your remote repository is more "recent" than your local.  Luckily, this is easily fixed.  

~~~
$git pull upstream master

$git status / git log --oneline

$git push upstream master
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

###Conflicts

Review: remotes, pushing, pulling// fork.  Draw a diagram on the board.  
Get everyone into original shell directory (?).  There should be a remote called origin and a 
remote called something else in your own directory.  Have everyone pull from her directory, push to backup

$git push backup master

$git pull origin master

Create conflict

Have everyone make a change in notes document, recall, you have to commit your changes. 
Instructions in etherpad:

1. Make a change in notes.txt - delete or add
2. Stage + commit 

$git add notes.txt, 
$git commit -m “my notes”
$git pull origin master

If everyone edited the same document, this will be a conflict.  

Try to push changes to Lynne’s repo.  

$git push origin master

Should fail.  Need to pull first.  
Resolve conflicts

$git pull is a combination of fetch + merge.  It’s the merge that we need to deal with now.  
If you’re in GitBash, you’ll see (master|MERGING) - that indicates that we’re in the middle of a merge.  
Let’s see where the conflicts are:

$git diff

$git status

Open that document.  

$notepad notes.txt

Git has put in some filler text.  
The cheap and easy way to resolve is just commit as is - do git add file and git commit -m “lazy merge”.  But that’s not actually what we want to do.  Edit the file so that it contains what you want.  You can pick among changes or make other changes.  Up to you.  Now add/commit.  

$git add notes.txt

$git commit -m “merging haiku document.”

same process as before.  

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

Have optional list of words on etherpad, so people can look it up if they get stuck.  
Local / Remote versions?  

$git init
$git add -A
$git add D.txt
$git commit -m “adding files”
$git status
$git log or $git log --oneline
$git diff (commit) (commit)
$git diff (commit) (commit) D.txt
$git branch new-branch
$git checkout new-branch
$git merge new-branch
$git checkout (commit) D.txt
$git branch or $git branch -v

Review
what are the two ways to create a repo online? (directly or via a fork)
what are the two ways to create a repo locally? (git init or cloning)
what are the two ways to link a local/remote? (use remote add or clone)
have worksheet?  

## Resources
branching app: http://pcottle.github.io/learnGitBranching/?NODEMO
atlassian: https://www.atlassian.com/git/tutorial/git-basics
git site: http://git-scm.com/
GUI interfaces - http://git-scm.com/downloads/guis
SWC site: http://software-carpentry.org/v5/novice/git/01-backup.html
diff visualizers, like https://sourcegear.com/diffmerge/
starlogs.net
