#include <stdio.h>

char	*ft_strrev(char *str);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		char *ret = ft_strrev(argv[i]);
		printf("[%s] returns_param=%d\n", argv[i], ret == argv[i]);
	}
	return (0);
}
