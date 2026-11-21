#include <unistd.h>

int	is_space(char c)
{
	return (c == ' ' || c == '\t');
}

int	main(int argc, char **argv)
{
	char	*s;
	int		i;
	int		start;
	int		end;
	int		printed;

	if (argc >= 2)
	{
		s = argv[1];
		i = 0;
		while (is_space(s[i]))
			i++;
		start = i;
		while (s[i] && !is_space(s[i]))
			i++;
		end = i;
		printed = 0;
		while (s[i])
		{
			while (is_space(s[i]))
				i++;
			if (!s[i])
				break ;
			if (printed)
				write(1, " ", 1);
			while (s[i] && !is_space(s[i]))
				write(1, &s[i++], 1);
			printed = 1;
		}
		if (end > start)
		{
			if (printed)
				write(1, " ", 1);
			write(1, s + start, end - start);
		}
	}
	write(1, "\n", 1);
	return (0);
}
