#include <stdio.h>
#include <string.h>

char	*ft_strcpy(char *s1, char *s2);

int	main(int argc, char **argv)
{
	char	buf[4096];

	for (int i = 1; i < argc; i++)
	{
		memset(buf, 'X', sizeof(buf));
		char *ret = ft_strcpy(buf, argv[i]);
		printf("[%s] returns_dest=%d terminated=%d\n", buf, ret == buf, buf[strlen(argv[i])] == '\0');
	}
	return (0);
}
