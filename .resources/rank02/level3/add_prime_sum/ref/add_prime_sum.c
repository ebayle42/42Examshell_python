#include <unistd.h>

int	is_prime(int n)
{
	int	i;

	if (n < 2)
		return (0);
	i = 2;
	while (i * i <= n)
	{
		if (n % i == 0)
			return (0);
		i++;
	}
	return (1);
}

void	put_nbr(int n)
{
	char	c;

	if (n >= 10)
		put_nbr(n / 10);
	c = n % 10 + '0';
	write(1, &c, 1);
}

int	main(int argc, char **argv)
{
	int	n;
	int	i;
	int	sum;

	sum = 0;
	if (argc == 2)
	{
		n = 0;
		i = 0;
		while (argv[1][i] >= '0' && argv[1][i] <= '9')
			n = n * 10 + argv[1][i++] - '0';
		while (n > 1)
		{
			if (is_prime(n))
				sum += n;
			n--;
		}
	}
	put_nbr(sum);
	write(1, "\n", 1);
	return (0);
}
