#include <unistd.h>

int	is_space(char c)
{
	return (c == ' ' || c == '\t');
}

void	capitalize(char *s)
{
	int		i;
	char	c;

	i = 0;
	while (s[i])
	{
		c = s[i];
		if (c >= 'A' && c <= 'Z')
			c += 32;
		if (c >= 'a' && c <= 'z' && (!s[i + 1] || is_space(s[i + 1])))
			c -= 32;
		write(1, &c, 1);
		i++;
	}
	write(1, "\n", 1);
}

int	main(int argc, char **argv)
{
	int	i;

	if (argc == 1)
		write(1, "\n", 1);
	i = 1;
	while (i < argc)
		capitalize(argv[i++]);
	return (0);
}
