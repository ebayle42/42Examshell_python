#include <stdio.h>
#include <stdlib.h>

char	*ft_itoa(int nbr);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		char *s = ft_itoa(atoi(argv[i]));
		printf("[%s]\n", s);
		free(s);
	}
	return (0);
}
