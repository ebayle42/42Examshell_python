#include <stdio.h>
#include <stdlib.h>

void	ft_swap(int *a, int *b);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
	{
		int a = atoi(argv[i]);
		int b = atoi(argv[i + 1]);
		ft_swap(&a, &b);
		printf("%d %d\n", a, b);
	}
	return (0);
}
