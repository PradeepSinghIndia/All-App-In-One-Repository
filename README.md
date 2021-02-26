# All-App-In-One-Repository

To tell Git who you are, run the following two commands:

     $ git config --global user.name "King Kong"
     $ git config --global user.email "king-kong@gmail.com"
     $ git config --list
  
 it's best to have some pretty colors for the output. To turn on code highlighting, just run the following command:

   $ git config --global color.ui true 
   
you've already created an empty directory for your project, you need to explicitly ask Git to create a safe deposit box – a repository – in that directory:
 Git will initialize a hidden directory called ".git" in the project's root directory.

       $ git init
    Initialized empty Git repository in /home/dell/new-folder/.git/
    
  You might want to know the status of your box: does it store anything yet? To know the Git status, you'll need to run:

    $ git status
  On branch master
Initial commit
nothing to commit (create/copy files and use "git add" to track)

To let Git track files for a commit, we need to run the following in the terminal:

          $ git add my_new_file.txt
  
  The option "--all" tells Git: "Find all new and updated files everywhere throughout the project and add them to the staging area." Note that you can also use the option "-A" instead of "--all". Thanks to this simple option, "-A" or "--all", the workflow is greatly simplified.
  
          $ git add --all or(-A)
  
   To remove files from the staging area, use the following command:

       $ git rm --cached my-file.ts

we specified the command "rm", which stands for remove. The "--cached" option indicates files in the staging area. Finally, we pass a file that we want to unstage. Git will output the following message for us:

         $ rm 'my_file.ts'
	 
You can consider "reset" as the opposite of "add".
   $ git reset another-file.js
  
 Let's start with a quick overview of committing to the Git repository. By now, you should have at least one file tracked by Git (we have three). As we mentioned, tracked files aren't located in the repository yet. We have to commit them: we need to carry our basket with stuff to the lock box. There are several useful Git commands to do (almost) the same: move (commit) files from the staging area (an imaginary basket) to the repository (a lock box).

There's nothing difficult about committing to a repository. Just run the following command:

          $ git commit -m "Add three files" 
	  
There will be times when you'll regret committing to a repository. Let's say you've modified ten files, but committed only nine. How can you add that remaining file to the last commit? And how can you modify a file if you've already committed it? There are two ways out. First, you can undo the commit:

   $ git reset --soft HEAD^      undo last commit	
   
   
   
   
   
  # You'll use several important Git commands to move (push) your code from a local repository to a remote repository and
  # to grab (pull) your team's collective code from a remote repository. 
    Now you need to bind this remote repository to your local repository:

         $ git remote add origin https://github.com/YourUsername/some-small-app.git
	 
	 
copying your code to a remote repository looks like this:

     $ git push -u origin master	
     
  Now that you've added a remote repository, you can view the list of repositories by running the following command:

     $ git remote -v 
   
   Git can clone an entire project from a remote repository. That's what the "clone" command does:

      $ git clone git@github.com:YourUsername/your-app.git
      $ git clone git@github.com:YourUsername/your-app.git this-name-is-much-better

Running "git pull" is enough to update your local repository.
   $ git pull
   
  
  
  Cloning a repository is very different from pulling from a repository. If you clone a remote repository, Git will:

Download the entire project into a specified directory; and
Create a remote repository called origin and point it to the URL you pass.
The last item simply means that you don't need to run "git remote add origin git@github.com:YourUsername/your-app.git" after cloning a repository. The "clone" command will add a remote origin automatically, and you can simply run "git push" from the repository.


When you run the "pull" command, Git will:

Pull changes in the current branch made by other developers; and
Synchronize your local repository with the remote repository.
The "pull" command doesn't create a new directory with the project name. Git will only pull updates to make sure that your the local repository is up to date.
   
   
   # BRANCHING
   Create a new branch to develop a new feature using "git branch <branch-name>".
Switch to the new branch from the main branch using "git checkout <branch-name>".
	$ git checkout master
          *master
          user-profile
This one command will let you create a new "admin-panel" branch and switch to that branch right away. Git earns another point for improving the workflow.
	
	$ git checkout -b admin-panel
	  
	 
  
  
  
  
  
    
    
   
