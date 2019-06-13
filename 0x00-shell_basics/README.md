# Basic Shell commands and script problems
## Review of basic shell commands based off of [concepts](http://linuxcommand.org/lc3_learning_the_shell.php) including:
* What is the Shell
* Navigation
* Looking Around
* Manipulating Files
* Working with Commands
### 0. Where am I?
> Write a script that prints the absolute path name of the current working directory.
### 1. What's in there?
> Display the contents list of your current directory.
### 2. There is no place like home
> Write a script that changes the working directory to the user’s home directory.
### 3. The long format
> Display current directory contents in a long format.
### 4. Hidden files
> Display current directory contents, including hidden files (starting with .). Use the long format.
### 5. I love numbers
> Display current directory contents.
### 6. Welcome holberton
> Create a script that creates a directory named holberton in the /tmp/ directory.
### 7. Betty in Holberton
> Move the file betty from /tmp/ to /tmp/holberton.
### 8. Bye bye Betty
> Delete the file betty (the file betty is in /tmp/holberton).
### 9. Bye bye Holberton
> Delete the directory holberton that is in the /tmp directory.
### 10. Back to the future.
> Write a script that changes the working directory to the previous one.
### 11. Lists
> Write a script that lists all files (even ones with names beginning with a period character, which are normally hidden) in the current directory and the parent of the working directory and the /boot directory (in this order), in long format.
### 12. File type
> Write a script that prints the type of the file named iamafile. The file iamafile will be in the /tmp directory when we will run your script.
### 13. We are symbols, and inhabit symbols
> Create a symbolic link to /bin/ls, named __ls__. The symbolic link should be created in the current working directory.
### 14. Copy HTML files
> Create a script that copies all the HTML files from the current working directory to the parent of the working directory, but only copy files that did not exist in the parent of the working directory or were newer than the versions in the parent of the working directory.
### 15. Let's Move
> Create a script that moves all files beginning with an uppercase letter to the directory /tmp/u.
### 16. Clean Emacs
> Create a script that deletes all files in the current working directory that end with the character ~.
### 17. Tree
> Create a script that creates the directories welcome/, welcome/to/ and welcome/to/holberton in the current directory.
### 18. Life is a series of commas, not periods
> Write a command that lists all the files and directories of the current directory, separated by commas (,).
> * Directory names should end with a slash (/)
> * Files and directories starting with a dot (.) should be listed
> * The listing should be alpha ordered, except for the directories . and .. which should be listed at the very beginning
> * Only digits and letters are used to sort; Digits should come first
> * You can assume that all the files we will test with will have at least one letter or one digit
The listing should end with a new line
### 19. File type: Holberton
> Create a magic file holberton.mgc that can be used with the command file to detect Holberton data files. Holberton data files always contain the string HOLBERTON at offset 0.