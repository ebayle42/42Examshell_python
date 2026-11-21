#include <stdio.h>
#include <stdlib.h>

char	**ft_split(char *str);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		char **tab = ft_split(argv[i]);
		int n = 0;
		printf("split:");
		while (tab[n])
		{
			printf(" [%s]", tab[n]);
			free(tab[n]);
			n++;
		}
		printf(" (%d words)\n", n);
		free(tab);
	}
	return (0);
}
