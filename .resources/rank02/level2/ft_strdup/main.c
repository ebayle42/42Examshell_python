#include <stdio.h>
#include <stdlib.h>

char	*ft_strdup(char *src);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		char *d = ft_strdup(argv[i]);
		printf("[%s] new_pointer=%d\n", d, d != argv[i]);
		free(d);
	}
	return (0);
}
