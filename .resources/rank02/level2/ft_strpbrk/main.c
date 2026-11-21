#include <stdio.h>

char	*ft_strpbrk(const char *s1, const char *s2);

int	main(int argc, char **argv)
{
	for (int i = 1; i + 1 < argc; i += 2)
	{
		char *p = ft_strpbrk(argv[i], argv[i + 1]);
		if (p)
			printf("index %ld\n", (long)(p - argv[i]));
		else
			printf("NULL\n");
	}
	return (0);
}
