#include <stdio.h>
#include <stdlib.h>

int	*ft_range(int start, int end);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
	{
		int start = atoi(argv[i]);
		int end = atoi(argv[i + 1]);
		int len = (start > end ? start - end : end - start) + 1;
		int *tab = ft_range(start, end);
		printf("(%d, %d):", start, end);
		for (int k = 0; k < len; k++)
			printf(" %d", tab[k]);
		printf("\n");
		free(tab);
	}
	return (0);
}
