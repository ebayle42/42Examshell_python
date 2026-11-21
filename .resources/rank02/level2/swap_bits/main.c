#include <stdio.h>
#include <stdlib.h>

unsigned char	swap_bits(unsigned char octet);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
		printf("%d\n", swap_bits((unsigned char)atoi(argv[i])));
	return (0);
}
