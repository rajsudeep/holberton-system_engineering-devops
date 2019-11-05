#include <stdlib.h>
#include <stdio.h>
#include <unistd.h>

/**
 * infinite_while - infinite looped delayed per 1 second
 * Return: On success 0 else 1
 */
int infinite_while(void)
{
	while (1)
	{
		sleep(1);
	}
	return (EXIT_SUCCESS);
}

/**
 * main - creates zombie processes
 * Return: On success 0 else 1
 */
int main(void)
{
	int i;
	pid_t child;

	for (i = 0; i < 5; i++)
	{
		child = fork();
		if (child > 0)
			printf("Zombie process created, PID: %i\n", child);
		else
			exit(EXIT_SUCCESS);
	}
	infinite_while();
	return (EXIT_SUCCESS);
}
