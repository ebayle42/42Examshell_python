#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>

void	print_bits(unsigned char octet);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		print_bits((unsigned char)atoi(argv[i]));
		write(1, "|", 1);
	}
	return (0);
}
