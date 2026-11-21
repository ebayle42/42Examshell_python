#include <unistd.h>

int	main(int argc, char **argv)
{
	int	seen[256];
	int	in2[256];
	int	i;

	if (argc == 3)
	{
		i = 0;
		while (i < 256)
		{
			seen[i] = 0;
			in2[i++] = 0;
		}
		i = 0;
		while (argv[2][i])
			in2[(unsigned char)argv[2][i++]] = 1;
		i = 0;
		while (argv[1][i])
		{
			if (in2[(unsigned char)argv[1][i]] && !seen[(unsigned char)argv[1][i]])
			{
				write(1, &argv[1][i], 1);
				seen[(unsigned char)argv[1][i]] = 1;
			}
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
