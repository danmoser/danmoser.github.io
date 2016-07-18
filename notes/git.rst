git
#####

.. contents:: Table of contents

Concepts
****************
Basics
=========
In short, the versions one has are:

- i) in the hard-disk, whenever you change a file;
- ii) a temporary (unnamed) version, when you do `git add .` (valid for each of the added files);
- iii) a permanent version, each time you do `git commit`.

The sincronization is:

- When you do `git pull`, all the committed versions from the server come to your hard-disk; 
- When you do `git push`, all the committed versions from hard-disk go to the server.


Other
======
- Commit your changes or stash them before you can switch branches.


Examples
***************
Cloning a repo
=================
.. code:: bash

    cd ~
    git clone https://github.com/danmoser/hello-world.git
    # or you can do
    git clone https://github.com/danmoser/hello-world.git destfolder
    
    # There is a change in the website, update it to your PC ('pull'):
    cd ~/hello-world
    git pull
    #    1 file changed, 1 insertion(+)


Create a new project
=====================
.. code:: bash

    # Start a new project
    cd project
    git init
    
    # to added to all files (in the current folder) to be tracked
    git add .
    
    # see status
    git status

    # -a/--all: Tell the command to automatically stage files that have been 
    # modified and deleted, but new files you have not told Git about are not affected.
    git commit -am "Commit 001"

Branches
==========
.. code:: bash

    # Create and switch to a new branch
    git branch develop
    # List branches
    git branch
    git branch -v
    # Switch to branch
    git checkout develop

    # Combining branches: NEVER rebase (unless you really know what you are doing)
    # Always **merge**
    # Merge branch into current (master)
    git checkout master
    git merge develop

    # When you merge a branch you are currently merging a the commits!
    # Show all commits
    git log
    git log --stat
    git log --oneline --decorate --graph --all
    # List commit id's
    git log --format="%h"

    # Delete branch "develop"
    git branch -d develop

Merge
===========
.. code:: bash

    # Someone made a merge request (github)
    # git checkout -b|-B <new_branch> [<start point>]
    # Specifying -b causes a new branch to be created as if git-branch[1] were 
    # called and then checked out. 
    git checkout -b dbednarski-newest master
    # Rename a branch
    git branch -m dbednarski-newest beacon-dnbed
    # The --no-ff flag prevents git merge from executing a "fast-forward" if it 
    # detects that your current HEAD is an ancestor of the commit you're trying to merge. 
    git checkout master
    # If you find the message *you need to resolve your current index first*, 
    # then edit the listed files looking for the >>> <<< entries.
    git merge --no-ff beacon-dnbed
    git push
    # git push origin master


General tips
=============
git ignore file extensions: 

.. code:: bash

    vim .git/info/exclude 
    # More info at 
    git help ignore

Ignore syncing `*.o` (but keep then at PC): 

.. code:: bash

    git rm --cached *.o -n  # `-n` is the dry-run
    # Use `--cached` to keep the file, or `-f` to force removal.

Roll back to a previous commit: `git reset --hard f2f730b`

.. code:: bash

    git diff --cached f2f730b arquivo.py

Dump old version file: 

.. code:: bash

    git cat-file -p cf1328e:./poltools.py > poltools.old.py

Add files from a remote local:

.. code:: bash

    git remote add origin https://github.com/USER/REPO.git

Upload your local commit to the web:

.. code:: bash

    git push origin master

Download the changes from the repository:

.. code:: bash

    git pull origin master


Refs
********
http://overapi.com/git

http://git-scm.com


Texts
=========
Rebase vs. merge
-----------------
Now that you've seen rebasing and merging in action, you may be wondering which one is better. Before we can answer this, let's step back a bit and talk about what history means.

One point of view on this is that your repository's commit history is a record of what actually happened. It's a historical document, valuable in its own right, and shouldn't be tampered with. From this angle, changing the commit history is almost blasphemous; you're lying about what actually transpired. So what if there was a messy series of merge commits? That's how it happened, and the repository should preserve that for posterity.

The opposing point of view is that the commit history is the story of how your project was made. You wouldn't publish the first draft of a book, and the manual for how to maintain your software deserves careful editing. This is the camp that uses tools like rebase and filter-branch to tell the story in the way that's best for future readers.

Now, to the question of whether merging or rebasing is better: hopefully you'll see that it's not that simple. Git is a powerful tool, and allows you to do many things to and with your history, but every team and every project is different. Now that you know how both of these things work, it's up to you to decide which one is best for your particular situation.

In general the way to get the best of both worlds is to rebase local changes you've made but haven't shared yet before you push them in order to clean up your story, but never rebase anything you've pushed somewhere.