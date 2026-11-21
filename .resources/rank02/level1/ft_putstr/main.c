#include <stdio.h>
#include <unistd.h>

void	ft_putstr(char *str);

int	main(int argc, char **argv)
{
	for (int i = 1; i < argc; i++)
	{
		fflush(stdout);
		ft_putstr(argv[i]);
		write(1, "|", 1);
	}
	return (0);
}
