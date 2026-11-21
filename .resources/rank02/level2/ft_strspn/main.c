#include <stdio.h>
#include <stddef.h>

size_t	ft_strspn(const char *s, const char *set);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
		printf("%zu\n", ft_strspn(argv[i], argv[i + 1]));
	return (0);
}
