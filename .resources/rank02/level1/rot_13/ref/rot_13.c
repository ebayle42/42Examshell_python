#include <unistd.h>

#define SHIFT 13

int	main(int argc, char **argv)
{
	int		i;
	char	c;

	if (argc == 2)
	{
		i = 0;
		while (argv[1][i])
		{
			c = argv[1][i];
			if (c >= 'a' && c <= 'z')
				c = (c - 'a' + SHIFT) % 26 + 'a';
			else if (c >= 'A' && c <= 'Z')
				c = (c - 'A' + SHIFT) % 26 + 'A';
			write(1, &c, 1);
			i++;
		}
	}
	write(1, "\n", 1);
	return (0);
}
