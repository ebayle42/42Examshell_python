#include <stdio.h>
#include <stdlib.h>

int	max(int *tab, unsigned int len);

int	main(int argc, char **argv)
{
	int	tab[1000];
	int	n = 0;

	for (int i = 1; i < argc; i++)
		tab[n++] = atoi(argv[i]);
	printf("%d\n", max(tab, n));
	printf("%d\n", max(tab, 0));
	return (0);
}
