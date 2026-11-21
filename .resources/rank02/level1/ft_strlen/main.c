#include <stdio.h>

int	ft_strlen(char *str);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
		printf("%d\n", ft_strlen(argv[i]));
	return (0);
}
