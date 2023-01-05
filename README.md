# GUIs - "graphical user interfaces"
This is a basic practice repo to start missing with and collaborating and building on GUI (graphical user interface), and to help with exploration and testing of github features, and how collaboration might work on a team of developers for creation of software etc.

# Below are generic instructions to add your local code to a github repo. When you connect to a github repo to start contributing, create your own seperate work branch and commit to that within the repo so that others can review your branch code and merge it into main branch after everything looks good. 

1. On your computer, move the file you'd like to upload to GitHub into the local directory that was created when you cloned the repository.
2. Open Git Bash in your terminal window in your editor.

3. Change the current working directory to your local repository.
4. Stage the file for commit to your local repository.
 ## $ git add .
Adds the file to your local repository and stages it for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.


5. Commit the file that you've staged in your local repository.
## $ git commit -m "Add existing file"
Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

6. Push the changes in your local repository to GitHub.com.
## $ git push origin YOUR_BRANCH
Pushes the changes in your local repository up to the remote repository you specified as the origin

# To connect to an existing repo use the remote connection to github repo within your editor, such as VS CODE. Once connected create your own branch and start commit and pushing to it.
# When you are ready to have your code reviewed, submit a pull request.

When you are testing this code in your local machine after cloning it to your local machine, make sure you are in the correct directory in your terminal window to ensure playback of the music file works. 
