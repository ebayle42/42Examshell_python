#include <stdio.h>
#include <stdlib.h>

int	is_power_of_2(unsigned int n);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		unsigned int n = (unsigned int)strtoul(argv[i], NULL, 10);
		printf("%u -> %d\n", n, is_power_of_2(n));
	}
	return (0);
}
