#include <stdio.h>
#include <stdlib.h>

unsigned int	lcm(unsigned int a, unsigned int b);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
	{
		unsigned int a = (unsigned int)strtoul(argv[i], NULL, 10);
		unsigned int b = (unsigned int)strtoul(argv[i + 1], NULL, 10);
		printf("lcm(%u, %u) = %u\n", a, b, lcm(a, b));
	}
	return (0);
}
