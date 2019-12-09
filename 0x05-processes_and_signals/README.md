## Processes and signals
### [0. What is my PID](./0-what-is-my-pid)
> Write a Bash script that displays its own PID
### [1. List your processes](./1-list_your_processes)
> Write a Bash script that displays a list of currently running processes
> * Must show all processes, for all users, including those which might not have a TTY
> * Display in a user-oriented format
> * Show process hierarchy
### [2. Show your Bash PID](./2-show_your_bash_pid)
> Using your previous exercise command, write a Bash script that displays lines containing the bash word, thus allowing you to easily get the PID of your Bash process
### [3. Show your Bash PID made easy](./3-show_your_bash_pid_made_easy)
> Write a Bash script that displays the PID, along with the process name, of processes whose name contain the word bash
### [4. To infinity and beyond](./4-to_infinity_and_beyond)
> Write a Bash script that displays To infinity and beyond indefinitely
### [5. Kill me now](./5-kill_me_now)
> Write a Bash script that kills [4-to_infinity_and_beyond](./4-to_infinity_and_beyond) process
> * You must use kill
### [6. Kill me now made easy](./6-kill_me_now_made_easy)
> Write a Bash script that kills 4-to_infinity_and_beyond process
> * You can't use kill or killall
### [7. Highlander](./7-highlander)
> Write a Bash script that displays:
> * To infinity and beyond indefinitely
> * With a sleep 2 in between each iteration
> * I am invincible!!! when receiving a SIGTERM signal
### [8. Beheaded process](./8-beheaded_process)
> Write a Bash script that kills the process 7-highlander
### [100. Process and PID file](./100-process_and_pid_file)
> Write a Bash script that:
> * Creates the file /var/run/holbertonscript.pid containing its PID
> * Displays To infinity and beyond indefinitely
> * Displays I hate the kill command when receiving a SIGTERM signal
> * Displays Y U no love me?! when receiving a SIGINT signal
> * Deletes the file /var/run/holbertonscript.pid and terminates itself when receiving a SIGQUIT or SIGTERM signal
### [102. Zombie](./102-zombie.c)
> Write a C program that creates 5 zombie processes
