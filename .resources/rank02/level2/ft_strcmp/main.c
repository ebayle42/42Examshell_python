#include <stdio.h>

int	ft_strcmp(char *s1, char *s2);

int	main(int argc, char **argv)
{
	/* only the sign of the result is compared, like the man page says */
	for (int i = 1; i + 1 < argc; i += 2)
	{
		int r = ft_strcmp(argv[i], argv[i + 1]);
		printf("%d\n", (r > 0) - (r < 0));
	}
	return (0);
}
