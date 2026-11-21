#include <unistd.h>

int	main(int argc, char **argv)
{
	int	seen[256];
	int	i;
	int	k;

	if (argc == 3)
	{
		i = 0;
		while (i < 256)
			seen[i++] = 0;
		k = 1;
		while (k <= 2)
		{
			i = 0;
			while (argv[k][i])
			{
				if (!seen[(unsigned char)argv[k][i]])
				{
					write(1, &argv[k][i], 1);
					seen[(unsigned char)argv[k][i]] = 1;
				}
				i++;
			}
			k++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
