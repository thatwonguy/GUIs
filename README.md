# GUIs
GUI exploration, and testing of github features

-On your computer, move the file you'd like to upload to GitHub into the local directory that was created when you cloned the repository.
-Open Git Bash.

-Change the current working directory to your local repository.
-Stage the file for commit to your local repository.
$ git add .
# Adds the file to your local repository and stages it for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.


-Commit the file that you've staged in your local repository.
$ git commit -m "Add existing file"
# Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.

-Push the changes in your local repository to GitHub.com.
$ git push origin YOUR_BRANCH
# Pushes the changes in your local repository up to the remote repository you specified as the origin
