#include <stdio.h>
#include <stdlib.h>

void	sort_int_tab(int *tab, unsigned int size);

int	main(int argc, char **argv)
{
	int	tab[1000];
	int	n = 0;

	for (int i = 1; i < argc; i++)
		tab[n++] = atoi(argv[i]);
	sort_int_tab(tab, n);
	for (int i = 0; i < n; i++)
		printf("%d ", tab[i]);
	printf("\n");
	return (0);
}
