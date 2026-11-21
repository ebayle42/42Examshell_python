#include <stdio.h>
#include <stdlib.h>

int	ft_atoi_base(const char *str, int str_base);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
		printf("%d\n", ft_atoi_base(argv[i], atoi(argv[i + 1])));
	return (0);
}
